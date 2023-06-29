# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 620)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ble_retransmission_button = QtWidgets.QPushButton(self.centralwidget)
        self.ble_retransmission_button.setGeometry(QtCore.QRect(680, 530, 111, 31))
        self.ble_retransmission_button.setStyleSheet(" QPushButton {\n"
"     \n"
"        \n"
"    background-color: rgb(255, 255, 127);\n"
"        padding: 5px;\n"
"        \n"
"    color: rgb(0, 0, 0);\n"
"        font: 25 10pt \"Arial Nova Cond Light\";\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #ffcc00;\n"
"        border-color: #ff9900;\n"
"        color: #ffffff;\n"
"        padding: 7px;\n"
"    }")
        self.ble_retransmission_button.setObjectName("ble_retransmission_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(19)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ble_tx_uuid = QtWidgets.QLineEdit(self.centralwidget)
        self.ble_tx_uuid.setGeometry(QtCore.QRect(160, 200, 221, 22))
        self.ble_tx_uuid.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-family: Arial, sans-serif; /* Default font family */\n"
"    font-size: 12px; /* Default font size */\n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_tx_uuid.setObjectName("ble_tx_uuid")
        self.ble_uuid = QtWidgets.QLineEdit(self.centralwidget)
        self.ble_uuid.setGeometry(QtCore.QRect(160, 140, 221, 22))
        self.ble_uuid.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-family: Arial, sans-serif; /* Default font family */\n"
"    font-size: 12px; /* Default font size */\n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_uuid.setObjectName("ble_uuid")
        self.ble_log_text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ble_log_text_edit.setEnabled(False)
        self.ble_log_text_edit.setGeometry(QtCore.QRect(620, 100, 271, 111))
        self.ble_log_text_edit.setStyleSheet("QPlainTextEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 5px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 25 10pt \"Arial Nova Cond Light\";\n"
"    \n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QPlainTextEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QPlainTextEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_log_text_edit.setObjectName("ble_log_text_edit")
        self.ble_disconnect_button = QtWidgets.QPushButton(self.centralwidget)
        self.ble_disconnect_button.setGeometry(QtCore.QRect(430, 190, 121, 31))
        self.ble_disconnect_button.setStyleSheet(" QPushButton {\n"
"        \n"
"        background-color: rgb(255, 85, 0);\n"
"  \n"
"        padding: 5px;\n"
"        color:  #ffffff;\n"
"font: 25 10pt \"Arial Nova Cond Light\";\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #ffcc00;\n"
"        border-color: #ff9900;\n"
"        color: #ffffff;\n"
"        padding: 7px;\n"
"    }")
        self.ble_disconnect_button.setObjectName("ble_disconnect_button")
        self.ble_name = QtWidgets.QLineEdit(self.centralwidget)
        self.ble_name.setGeometry(QtCore.QRect(160, 110, 221, 22))
        self.ble_name.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-family: Arial, sans-serif; /* Default font family */\n"
"    font-size: 12px; /* Default font size */\n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_name.setObjectName("ble_name")
        self.ble_rx_uuid = QtWidgets.QLineEdit(self.centralwidget)
        self.ble_rx_uuid.setGeometry(QtCore.QRect(160, 170, 221, 22))
        self.ble_rx_uuid.setStyleSheet("QLineEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-family: Arial, sans-serif; /* Default font family */\n"
"    font-size: 12px; /* Default font size */\n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_rx_uuid.setObjectName("ble_rx_uuid")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 240, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(19)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ble_connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.ble_connect_button.setGeometry(QtCore.QRect(430, 110, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.ble_connect_button.setPalette(palette)
        self.ble_connect_button.setStyleSheet(" QPushButton {\n"
"     \n"
"        background-color: rgb(0, 170, 127);\n"
"        padding: 5px;\n"
"        color:  #ffffff;\n"
"        font: 25 10pt \"Arial Nova Cond Light\";\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #ffcc00;\n"
"        border-color: #ff9900;\n"
"        color: #ffffff;\n"
"        padding: 7px;\n"
"    }")
        self.ble_connect_button.setObjectName("ble_connect_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(19)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 135, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ble_corrupted_text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ble_corrupted_text_edit.setEnabled(False)
        self.ble_corrupted_text_edit.setGeometry(QtCore.QRect(610, 290, 281, 141))
        self.ble_corrupted_text_edit.setStyleSheet("QPlainTextEdit {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 5px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 25 10pt \"Arial Nova Cond Light\";\n"
"    \n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QPlainTextEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QPlainTextEdit::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_corrupted_text_edit.setObjectName("ble_corrupted_text_edit")
        self.ble_scan_devices_button = QtWidgets.QPushButton(self.centralwidget)
        self.ble_scan_devices_button.setGeometry(QtCore.QRect(140, 480, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.ble_scan_devices_button.setPalette(palette)
        self.ble_scan_devices_button.setStyleSheet(" QPushButton {\n"
"         \n"
"        background-color: rgb(0, 85, 127);\n"
"        padding: 5px;\n"
"        color:  #ffffff;\n"
"        font: 25 10pt \"Arial Nova Cond Light\";\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #ffcc00;\n"
"        border-color: #ff9900;\n"
"        color: #ffffff;\n"
"        padding: 7px;\n"
"    }")
        self.ble_scan_devices_button.setObjectName("ble_scan_devices_button")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 240, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(19)
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.ble_devices_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.ble_devices_table_widget.setGeometry(QtCore.QRect(20, 290, 361, 181))
        self.ble_devices_table_widget.setStyleSheet("QTableWidget {\n"
"    background-color: #f5f5f5; /* Default background color */\n"
"    border: 5px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 25 10pt \"Arial Nova Cond Light\";\n"
"    \n"
"    color: #333333; /* Default text color */\n"
"}\n"
"\n"
"QTableWidget:focus {\n"
"    border-color: #ff9900; /* Border color when focused */\n"
"}\n"
"\n"
"QTableWidget::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"\n"
"QTableWidget::hover {\n"
"    background-color: #ffffff; /* Background color when hovered */\n"
"    border-color: #ff9900; /* Border color when hovered */\n"
"    color: #333333; /* Text color when hovered */\n"
"}")
        self.ble_devices_table_widget.setObjectName("ble_devices_table_widget")
        self.ble_devices_table_widget.setColumnCount(2)
        self.ble_devices_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ble_devices_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ble_devices_table_widget.setHorizontalHeaderItem(1, item)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(600, 440, 291, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.ble_speed_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ble_speed_label.setStyleSheet("font: 25 11pt \"Arial Nova Cond Light\";")
        self.ble_speed_label.setText("")
        self.ble_speed_label.setObjectName("ble_speed_label")
        self.horizontalLayout.addWidget(self.ble_speed_label)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(370, 510, 215, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(380, 540, 201, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.incoming_crc_line_edit = QtWidgets.QLineEdit(self.widget1)
        self.incoming_crc_line_edit.setObjectName("incoming_crc_line_edit")
        self.horizontalLayout_3.addWidget(self.incoming_crc_line_edit)
        self.calculated_crc_line_edit = QtWidgets.QLineEdit(self.widget1)
        self.calculated_crc_line_edit.setObjectName("calculated_crc_line_edit")
        self.horizontalLayout_3.addWidget(self.calculated_crc_line_edit)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(770, 470, 121, 27))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial Nova Cond Light")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.sps_label = QtWidgets.QLabel(self.widget2)
        self.sps_label.setText("")
        self.sps_label.setObjectName("sps_label")
        self.horizontalLayout_4.addWidget(self.sps_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.ble_retransmission_button.setText(_translate("MainWindow", "Retransmission"))
        self.label_6.setText(_translate("MainWindow", "Message Log"))
        self.ble_disconnect_button.setText(_translate("MainWindow", "BLE Disconnect"))
        self.label_9.setText(_translate("MainWindow", "Corrupted Messages"))
        self.ble_connect_button.setText(_translate("MainWindow", "BLE Connect"))
        self.label_5.setText(_translate("MainWindow", "Credentials"))
        self.label.setText(_translate("MainWindow", "Device Name"))
        self.label_2.setText(_translate("MainWindow", "UART Service UUID"))
        self.label_3.setText(_translate("MainWindow", "UART RX Char UUID"))
        self.label_4.setText(_translate("MainWindow", "UART TX Char UUID"))
        self.ble_scan_devices_button.setText(_translate("MainWindow", "BLE Scan"))
        self.label_10.setText(_translate("MainWindow", "Devices"))
        item = self.ble_devices_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key"))
        item = self.ble_devices_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.label_7.setText(_translate("MainWindow", "Number of Incoming Messages p/s :"))
        self.label_8.setText(_translate("MainWindow", "Incoming CRC |"))
        self.label_11.setText(_translate("MainWindow", "Calculated CRC"))
        self.label_12.setText(_translate("MainWindow", "Sample p/s :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())