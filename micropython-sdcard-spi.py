# Mount and read a SPI-based SD card reader in MicroPython

# requires sdcard.py from https://github.com/micropython/micropython-lib

import machine, os
from sdcard import SDCard

# *************** pi pico ***************
# define pins
# from what I gather, if using the default pins for the SPI slot (eg 0 in this case)
# the sck, mosi and miso ports aren't required to be defined.
# spi_sck = machine.Pin(18) 
# spi_mosi = machine.Pin(19) 
# spi_miso = machine.Pin(16) 

# if using default pins for the given SPI slot, only cs needs to be defined
spi_cs = machine.Pin(17)

# create the spi instance
thisSPI = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)

# create the sdcard instance
thisCard = SDCard(thisSPI, spi_cs)

# Mount the SD card instance
os.mount(thisCard, "/sd")

# list using os.listdir()
print(os.listdir("/sd"))
# *************** pi pico end ***********


# *************** esp32wroom ***************
# some ESP32s have 2 SPI buses, HSPI and VSPI, and I always forget which maps to which SPI number..
# VSPI: MOSI → GPIO23, MISO → GPIO19, SCLK → GPIO18, CS → GPIO5 (SPI3) <<-- not present on my ESP32WROOM?
# HSPI: MOSI → GPIO13, MISO → GPIO12, SCLK → GPIO14, CS → GPIO15 (SPI2) <<-- this one works 100% on my board

spi_cs = machine.Pin(15)

# it looks like you have to define the other 3 pins in the args for the SPI instance on esp32, 
# whereas on the pi pico it's happy with just the SPI Bus ID...

spi_sck=machine.Pin(14)
spi_mosi=machine.Pin(13)
spi_miso=machine.Pin(12)

# create the spi instance
thisSPI = machine.SPI(2, 10000000, sck=spi_sck, mosi=spi_mosi, miso=spi_miso)

# create the sdcard instance
thisCard = SDCard(thisSPI, spi_cs)

# Mount the SD card instance
os.mount(thisCard, "/sd")

# list using os.listdir()
print(os.listdir("/sd"))

# *************** esp32wroom end ***********