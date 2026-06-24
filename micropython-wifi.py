# wifi setup on MicroPython

# imports
import network
import config # optional, uses config.py to store ssid/password

# set up hardware
station = network.WLAN(network.STA_IF)
station.active(True)

# set ssid/password
ssid = "mySSID" # hard coded
ssid = config.ssid # from a config.py file

password = "myPassword" # hard coded
ssid = config.password # from a config.py file

# connect
station.connect(ssid, password)

# connect to wifi
while not station.isconnected():
    print('Connecting....')
    pass

# show IP address
print('Connected to Wi-Fi:', station.ifconfig())
myIP = station.ipconfig("addr4")[0]

# Works on esp32 and pi pico w
