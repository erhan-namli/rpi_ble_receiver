# Installation

- Create a virtual environment 

```
python -m venv testenv
```

- Install the requirements

```
pip install requirements.txt
```

# Run
```
python gui_app.py
```

pyuic5 -x main_window.ui -o main_window.py

## Using

- Firstly scan the ble devices over the area by pressing the BLE Scan button
- Secondly, when you see your device just click on that device address and it automatically goes to the BLE NAME line
- Press the connect button and see your devices services
- Choose one of your device's service(which in this scenario must be a notify service)
- Press the notify button and see your SPS and incoming messages per second on the GUI.  