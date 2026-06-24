# misc micropython snippets eg 2 line LCD init, examples etc

# ****************************************************************************************
# setup 2 line LCD over I2C
# requires machine_i2c_lcd.py and lcd_api.py from https://github.com/dhylands/python_lcd
# ** Imports:
from machine_i2c_lcd import I2cLcd
import lcd_api
from machine import Pin, I2C
# **
# Define the LCD I2C address and dimensions
i2cAddress = 0x27
ic2Rows = 2
i2cCols = 16

# Initialize I2C and LCD objects
i2c = I2C(1, sda=Pin(21), scl=Pin(22))
lcd = I2cLcd(i2c, i2cAddress, ic2Rows, i2cCols)

# show a welcome message
lcd.move_to(0, 0)
lcd.putstr("Welcome!")

# ^^ this works on ESP32. Haven't checked on Pi Pico but should work with relevant pins
# ****************************************************************************************

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# ****************************************************************************************
# setup sh1106 or similar OLED over i2c
# requires sh1106.py from https://github.com/robert-hh/SH1106
# ** Imports:
from machine import Pin, I2C
import sh1106

# Define the OLED I2C address and dimensions
oledW = 128
oledH = 64
oledAddress = 0x3c
i2c = I2C(1, sda=Pin(21), scl=Pin(22)) # <-- ESP32
i2c = I2C(1, sda=Pin(14), scl=Pin(15)) # <-- Pi Pico
oledDisplay = sh1106.SH1106_I2C(oledW, oledH, i2c, None, oledAddress, rotate=0, delay=0)
oledDisplay.init_display()

# the .text function takes the string, x postion, y position and optionally colour as arguments
# show a welcome message
oledDisplay.text('Welcome', 0, 0, 1)
oledDisplay.text('to the', 0, 10, 1)
oledDisplay.text('Jungle', 0, 19, 1)
oledDisplay.show()
# to clear, use this:
# oledDisplay.fill(0) # <-- doesn't seem to work?

# ^^ this works on ESP32 and Pi Pico
# ****************************************************************************************
