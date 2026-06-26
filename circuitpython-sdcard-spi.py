# Mount and read a SPI-based SD card reader in CircuitPython

# required files:

import busio
import sdcardio
import storage
import os

# *************** pi pico ***************
# define pins
# from what I gather, if using the default pins for the SPI slot (eg 0 in this case)
# the sck, mosi and miso ports aren't required to be defined.
spi_sck = GP10
spi_mosi = GP11
spi_miso = GP12
spi_cs = GP15

#create the SPI instance
thisSPI = busio.SPI(clock=spi_sck, MOSI=spi_mosi, MISO=spi_miso)

# create the SD card instance
thisSDCard = sdcardio.SDCard(thisSPI, spi_cs)
 
# set the virtual file system
myCardFS = storage.VfsFat(thisSDCard)

#mount the filesystem
storage.mount(myCardFS, '/sd')

# show the contents
os.listdir('/sd')

# *************** pi pico end ***********


# *************** esp32wroom ***************
# Note to avoid head vs wall moments!
# 1. The SD card readers I have need to have VCC connected to VIN on the board - 3V3 doesn't provide enough juice
# 2. some ESP32s have 2 SPI buses, HSPI and VSPI, and I always forget which maps to which SPI number..
# VSPI: MOSI → GPIO23, MISO → GPIO19, SCLK → GPIO18, CS → GPIO5 (SPI3) <<-- not present on my ESP32WROOM?
# HSPI: MOSI → GPIO13, MISO → GPIO12, SCLK → GPIO14, CS → GPIO15 (SPI2) <<-- this one works 100% on my board
#TBD

# *************** esp32wroom end ***********