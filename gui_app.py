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

        self.ui.ble_disconnect_button.clicked.connect(self.handle_disconnect)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.call_function)  # Connect the timer to the function
    
        # Start the timer with a one-second interval
        timer.start(2000)  # 1000 milliseconds = 1 second

        self.connect_device = JobThread(self.conn_device)

        self.ui.ble_connect_button.clicked.connect(self.connect_ble_function)

        self.current_device = ""

        self.current_UUID = ""

        self.ui.ble_devices_table_widget.currentItemChanged.connect(self.table_device_choose_function)

        self.ui.ble_characteristics_table_widget.currentItemChanged.connect(self.table_char_choose_function)

        self.ui.ble_uuid_notify.clicked.connect(self.start_notify)
        
        self.incoming_crc_v = ""

        self.calculated_crc_v = ""

        self.DATA_PACKET_SIZE = 41

        self.CHUNK_SIZE = 12

        self.ble_speed_byte = 0

        self.ble_sps = 0

        self.device_notify_flag = False

    def start_notify(self):

        self.device_notify_flag = True

    def table_char_choose_function(self, item):

        if item is not None:
            value = item.text()
            print("Clicked item value:", value)

            self.ui.ble_uuid.setText(value)

            self.current_UUID = value

    def table_device_choose_function(self, item):

        if item is not None:
            value = item.text()
            print("Clicked item value:", value)

            self.ui.ble_name.setText(value)

            self.current_device = value

    def call_function(self):

        print(self.ble_speed_byte)

        self.ui.sps_label.setText(str(self.ble_speed_byte*self.CHUNK_SIZE))


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

    def populate_table_uuid(self, services):

        self.ui.ble_uuids_table_widget.setRowCount(3)

        for row, service in enumerate(services):

            uuid_item = QTableWidgetItem(str(service.uuid))
            self.ui.ble_uuids_table_widget.setItem(row, 0, uuid_item)

        # TO DO
        # - services

        pass

    def populate_table_characteristics(self, services):

        self.ui.ble_characteristics_table_widget.setRowCount(10)

        for service in services:
            print("Service UUID:", service.uuid)
            print("Characteristics:")
            for row, char in enumerate(service.characteristics):
                print("\tCharacteristic UUID:", char.uuid)
                char_item = QTableWidgetItem(str(char.uuid))
                self.ui.ble_characteristics_table_widget.setItem(row, 0, char_item)
                print("\tProperties:", char.properties)

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

                #print("Incoming CRC HEX", hex(crc_incoming))

                if(crc_check != crc_incoming):

                    self.ui.crc_check_box.setChecked(False)

                    print("INCOMING CRC", crc_incoming, "Calculated CRC", crc_check)
                    
                elif(crc_check == crc_incoming):

                    self.ui.crc_check_box.setChecked(True)



    def handle_disconnect(self, _: BleakClient):
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

            #print(f"Messages per second: {message_count / elapsed_time:.2f}")

            speed = message_count / elapsed_time

        except ZeroDivisionError:

            speed = 0

        self.ble_speed_byte = round(speed)

        self.ui.ble_speed_label.setText(str(round(speed)))

        self.parse_incoming_data(data)
        
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
                    
                    services = await client.get_services()

                    self.populate_table_uuid(services)

                    self.populate_table_characteristics(services)

                    while True:

                        if self.device_notify_flag == True:
                            print("START NOTIFY")
                            await client.start_notify(self.current_UUID, self.notification_handler)
                            await asyncio.sleep(int(self.ui.ble_connection_time_combo_box.currentText()))

                        else:
                            
                            print("NO NOTIFY")
                            pass

                        #await asyncio.sleep(int(self.ui.ble_connection_time_combo_box.currentText()))  # Listen for 10 seconds

                    #await asyncio.sleep(5)  # Listen for 10 seconds
                    #await client.stop_notify("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")          

                    # nus = client.services.get_service(UART_SERVICE_UUID)
                    # rx_char = nus.get_characteristic(UART_RX_CHAR_UUID)
                    
                    # for s in sliced("data", rx_char.max_write_without_response_size):
                    #     await client.write_gatt_char(rx_char, s)

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