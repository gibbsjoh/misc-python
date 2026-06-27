# Mount and read a SPI-based SD card reader in CircuitPython

# required files:

import busio
import sdcardio
import storage
import os

# *************** pi pico ***************
# define pins
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

# NOTE!! I seem to be stuck in a loop where I can't disable the USB disk mode that CP "helpfully" enables but that means I can't mount the SD card..
# So this is WIP!!

# Note to avoid head vs wall moments!
# 1. The SD card readers I have need to have VCC connected to VIN on the board - 3V3 doesn't provide enough juice
# 2. some ESP32s have 2 SPI buses, HSPI and VSPI, and I always forget which maps to which SPI number..
# VSPI: MOSI → GPIO23, MISO → GPIO19, SCLK → GPIO18, CS → GPIO5 (SPI3) <<-- not present on my ESP32WROOM?
# HSPI: MOSI → GPIO13, MISO → GPIO12, SCLK → GPIO14, CS → GPIO15 (SPI2) <<-- this one works 100% on my board

# # define pins
# spi_sck = GP14
# spi_mosi = GP13
# spi_miso = GP12
# spi_cs = GP15

# #create the SPI instance
# thisSPI = busio.SPI(clock=spi_sck, MOSI=spi_mosi, MISO=spi_miso)

# # create the SD card instance
# thisSDCard = sdcardio.SDCard(thisSPI, spi_cs)
 
# # set the virtual file system
# myCardFS = storage.VfsFat(thisSDCard)

# #mount the filesystem
# storage.mount(myCardFS, '/sd')

# # show the contents
# os.listdir('/sd')

# *************** esp32wroom end ***********