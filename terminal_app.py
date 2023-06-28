import asyncio
import sys
import time
from itertools import count, takewhile
from typing import Iterator
import struct
import datetime

from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

message_count = 0
start_time = 0


ESP_NAME = "UART Device"

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

# Get the current date and time
current_datetime = datetime.datetime.now()

# Create the filename based on the current date and time
filename = current_datetime.strftime("%Y-%m-%d_%H-%M-%S.csv")

# TIP: you can get this function and more from the ``more-itertools`` package.


def sliced(data: bytes, n: int) -> Iterator[bytes]:
    """
    Slices *data* into chunks of size *n*. The last slice may be smaller than
    *n*.
    """
    return takewhile(len, (data[i: i + n] for i in count(0, n)))

def calculate_incoming_crc(data):
    DATA_PACKET_SIZE = 41
    # CRC parameters
    polynomial = 0x1021
    crc = 0xFFFF

    # Calculate CRC for each byte in the data packet
    for i in range(DATA_PACKET_SIZE - 2):
        
        crc ^= (data[i] << 8)
        for j in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFFFF  # Ensure the CRC remains within 16 bits
    #print("HEX CRC", hex(crc))  # Output the calculated CRC value
    return crc

def parse_incoming_data(data_main):

    if len(data_main) % 41 == 0:
                # loop through the data_main and extract the data
            for i in range(0, len(data_main), 41):
                data = data_main[i:i+41]
                #print(data)
                
                id_value = struct.unpack("<I", data[:2]  + b"\x00\x00")[0]
                ads_channel = [0, 0, 0, 0, 0, 0, 0, 0]
                ads_channel[0] = struct.unpack(
                        "<I", data[2:5] + b"\x00")[0]
                ads_channel[1] = struct.unpack(
                        "<I", data[5:8] + b"\x00")[0]
                ads_channel[2] = struct.unpack(
                        "<I", data[8:11] + b"\x00")[0]
                ads_channel[3] = struct.unpack(
                        "<I", data[11:14] + b"\x00")[0]
                ads_channel[4] = struct.unpack(
                        "<I", data[14:17] + b"\x00")[0]
                ads_channel[5] = struct.unpack(
                        "<I", data[17:20] + b"\x00")[0]
                ads_channel[6] = struct.unpack(
                        "<I", data[20:23] + b"\x00")[0]
                ads_channel[7] = struct.unpack(
                        "<I", data[23:26] + b"\x00")[0]
                time_stamp = struct.unpack("<I", data[26:29] + b"\x00")[0]
                rskin = struct.unpack("<I", data[29:32] + b"\x00")[0]
                heart_rate = struct.unpack("<I", data[32:35] + b"\x00")[0]
                battery = struct.unpack("<I", data[35:37] + b"\x00\x00")[0]
                temperature = struct.unpack(
                        "<I", data[37:39] + b"\x00\x00")[0]
                    
                crc_incoming = struct.unpack("<I",   data[39:41] + b"\x00\x00" )[0]

                ##print("REVERSED", data[41:39:-1])

                crc_check = calculate_incoming_crc(data)

                print("Incoming CRC HEX", hex(crc_incoming))

                if(crc_check != crc_incoming):

                    print("CRC Check Failed")

                    print("INCOMING CRC", crc_incoming, "Calculated CRC", crc_check)
                
                elif(crc_check == crc_incoming):

                    print("CRC Verified")

                    # Create a single string containing all the unpacked values, separated by commas
                #unpacked_data = f"{id_value},{','.join(map(str, ads_channel))},{time_stamp},{rskin},{heart_rate},{battery},{temperature}\n"

            
async def uart_terminal(esp_name):
    while True:
        device = await BleakScanner.find_device_by_name(esp_name)

        if device is None:
            print("No matching device found, you may need to edit match_nus_uuid().")
            await asyncio.sleep(1)
            continue

        def handle_disconnect(_: BleakClient):
            print("Device was disconnected, reconnecting...")
            # Cancelling all tasks effectively ends the program
            for task in asyncio.all_tasks():
                task.cancel()

        def handle_rx(_: BleakGATTCharacteristic, data_main: bytearray):

            global message_count, start_time
    
            message_count += 1
            if start_time == 0:
                start_time = time.time()
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            #print(f"Received data: {data_main}")
            print(f"Messages per second: {message_count / elapsed_time:.2f}")

            parse_incoming_data(data_main)

        async with BleakClient(device, disconnected_callback=handle_disconnect) as client:
            await client.start_notify(UART_TX_CHAR_UUID, handle_rx)

            print("Connected, start typing and press ENTER")

            loop = asyncio.get_running_loop()
            nus = client.services.get_service(UART_SERVICE_UUID)
            rx_char = nus.get_characteristic(UART_RX_CHAR_UUID)

            while True:
                data = await loop.run_in_executor(None, sys.stdin.buffer.readline)

                # Data will be empty on EOF (e.g., CTRL+D on *nix)
                if not data:
                    break

                for s in sliced(data, rx_char.max_write_without_response_size):
                    await client.write_gatt_char(rx_char, s)

                print("Sent:", data)


if __name__ == "__main__":
    try:
        while True:
            asyncio.run(uart_terminal(ESP_NAME))
            print("Disconnected, reconnecting...")
            time.sleep(1)
    except asyncio.CancelledError:
        # Task is cancelled on disconnect, so we ignore this error
        pass
