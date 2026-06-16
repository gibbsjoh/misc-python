# misc micropython snippets eg 2 line LCD init, examples etc

# setup 2 line LCD over I2C
# requires machine_i2c_lcd.py:
# and lcd_api.py: 
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

