import sys
import asyncio
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QLabel, QWidget, QComboBox, QTextEdit, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt, QPoint, QThread, pyqtSignal, QTimer

from bleak import BleakClient, BleakScanner, discover
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

import time
import struct

ESP_NAME = "UART Device"

message_count = 0
start_time = 0

global_incoming_crc = 0

global_calculated_crc = 0

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

from main_window import Ui_MainWindow

class Config_BLE(Ui_MainWindow, QMainWindow, QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.ble_connect_button.clicked.connect(self.connect_ble_function)

        self.ui.ble_connect_button.clicked.connect(self.disconnect_ble_function)

        self.ui.ble_scan_devices_button.clicked.connect(self.scan_now)

        timer = QtCore.QTimer()
        timer.timeout.connect(self.call_function)  # Connect the timer to the function
    
        # Start the timer with a one-second interval
        timer.start(100)  # 1000 milliseconds = 1 second

        self.connect_device = JobThread(self.conn_device)

        self.ui.ble_connect_button.clicked.connect(self.connect_ble_function)

        self.current_device = "9C:9C:1F:C7:F2:6A"

        self.current_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"

        self.incoming_crc_v = ""

        self.calculated_crc_v = ""

        self.DATA_PACKET_SIZE = 41

        self.ble_speed_byte = 0

        self.ble_sps = 0

    def call_function(self):

        self.ui.sps_label.setText("Erhann")


    def connect_ble_function(self):

        self.connect_device.start()

        pass

    def disconnect_ble_function(self):
        pass

    def scan_now(self):
        """ Get BLE address and device name from available BLE advertisement

        :return: list of ble devices
        """
        async def ble_scan():
            devices = await discover()
            dev_list = []
            for dev in devices:
                dev_list.append(str(dev))
            return dev_list
        loop = asyncio.new_event_loop()
        devices = loop.run_until_complete(ble_scan())
        loop.close()
        self.parse_address(devices)

        self.populate_table(devices)

    def parse_address(self, devices):
        """ Parse and store data of BLE devices on a dictionary where the device name is the key
            and BLE address is the value
        :param devices: list of devices

        :return: None
        """
        for dev in devices:
            dev  = dev.split(' ')
            addr = dev[0].strip().strip(':')
            dev  = ''.join([s.strip() for s in dev[1:]])

    def populate_table(self, devices):

        self.ui.ble_devices_table_widget.setRowCount(len(devices))

        for row, data in enumerate(devices):
            key, value = data.split(": ")
            key_item = QTableWidgetItem(key.strip(" '"))
            value_item = QTableWidgetItem(value.strip(" '"))

            self.ui.ble_devices_table_widget.setItem(row, 0, key_item)
            self.ui.ble_devices_table_widget.setItem(row, 1, value_item)

    def calculate_incoming_crc(self, data):

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
    
    def parse_incoming_data(self, data_main):

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

                crc_check = self.calculate_incoming_crc(data)

                print("Incoming CRC HEX", hex(crc_incoming))

                if(crc_check != crc_incoming):

                    print("CRC Check Failed")

                    print("INCOMING CRC", crc_incoming, "Calculated CRC", crc_check)
                    
                elif(crc_check == crc_incoming):

                    print("CRC Verified")

                    self.incoming_crc_v = crc_incoming

                    self.calculated_crc_v = crc_check


    def handle_disconnect(_: BleakClient, self):
        print("Device was disconnected, goodbye.")
        # cancelling all tasks effectively ends the program
        for task in asyncio.all_tasks():
            task.cancel()

    async def notification_handler(self, sender, data):

        global message_count, start_time

        message_count += 1
        if start_time == 0:
            start_time = time.time()
        current_time = time.time()
        elapsed_time = current_time - start_time

        try:

            print(f"Messages per second: {message_count / elapsed_time:.2f}")

            speed = message_count / elapsed_time

        except ZeroDivisionError:

            speed = 0

        self.ui.ble_speed_byte = round(speed)

        self.ui.ble_speed_label.setText(str(round(speed)))

        self.parse_incoming_data(data)

        # self.ui.incoming_crc_line_edit.setText(str(hex(self.incoming_crc_v)))

        # self.ui.calculated_crc_line_edit.setText(str(hex(self.calculated_crc_v)))

        #print("received:", data)
        
    def handle_rx(sender: BleakGATTCharacteristic, data: bytearray, self):

        pass

    def conn_device(self):
            """ Thread for establishing connection to selected BLE device, once connected it will continuously read values
                for the selected mode.

            :return: None
            """
            async def conn(address, loop, self):

                # Use Pybleak to access GATT
                async with BleakClient(address, loop=loop, disconnected_callback=self.handle_disconnect) as client:
                    ## 1
                    # await client.start_notify(UART_TX_CHAR_UUID, self.handle_rx)
                    # print("Connected, start typing and press ENTER")

                    await client.start_notify("6E400003-B5A3-F393-E0A9-E50E24DCCA9E", self.notification_handler)
                    await asyncio.sleep(40)  # Listen for 10 seconds
                    #await client.stop_notify("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")          

                    # nus = client.services.get_service(UART_SERVICE_UUID)
                    # rx_char = nus.get_characteristic(UART_RX_CHAR_UUID)
                    
                    # for s in sliced("data", rx_char.max_write_without_response_size):
                    #     await client.write_gatt_char(rx_char, s)

                    time.sleep(0.2)

            loop = asyncio.new_event_loop()
            self.flag = False

            print("debug1")

            # Try connecting to device until it succeed
            while not self.flag:
                try:
                    print("debug2")
                    loop.run_until_complete(conn(self.current_device, loop, self))
                    
                except:
                    time.sleep(0.02)

class JobThread(QThread):
    """
        Thread class for performing long process tasks
    """
    signal = pyqtSignal()

    def __init__(self, job):
        QThread.__init__(self)
        self.job = job

    def run(self):
        self.job()

        self.signal.emit()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setApplicationDisplayName("BLE Config App")

    MainWindow = Config_BLE()

    MainWindow.show()

    sys.exit(app.exec_())