import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

def call_function():
    print("This function is called every one second.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Create a QTimer object
    timer = QTimer()
    timer.timeout.connect(call_function)  # Connect the timer to the function
    
    # Start the timer with a one-second interval
    timer.start(1000)  # 1000 milliseconds = 1 second
    
    # Run the application event loop
    sys.exit(app.exec_())