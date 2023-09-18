# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on Tue Dec  4  2018 - 00:43:55

@author: Jackson Alessandro dos Santos
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#import smbus
#import time
#import serial    # para usar com Arduino
import RPi.GPIO as gpio
import datetime

#arduino = serial.Serial('/dev/ttyACM0', 9600)

# Config das portas
gpio.setmode(gpio.BOARD)   # Contagem do PINOUT, no. GPIO (BCM/BOARD)
gpio.setup(x, gpio.IN)

#BOARD - BCM - DESCRIBE
#01 - 3.3v
#02 - 5v
#03 - GPIO02 - SDA1 - I2C
#04 - 5v
#05 - GPIO03 - SCL1 - I2C
#06 - Ground
#07 - GPIO04 - GPIO_GCLK
#08 - GPIO14 - TXD0
#09 - Ground
#10 - GPIO15 - RXD0
#11 - GPIO17 - GPIO_GEN0
#12 - GPIO18 - GPIO_GEN1
#13 - GPIO27 - GPIO_GEN2
#14 - Ground
#15 - GPIO22 - GPIO_GEN3
#16 - GPIO23 - GPIO_GEN4
#17 - 3.3v
#18 - GPIO24 - GPIO_GEN5
#19 - GPIO10 - SPI_MOSI
#20 - Ground
#21 - GPIO09 - SPI_MISO
#22 - GPIO25 - GPIO_GEN6
#23 - GPIO11 - SPI_CLK
#24 - GPIO08 - SPI_CE0_N
#25 - Ground
#26 - GPIO07 - SPI_CE1_N
#27 - ID_SD - I2C ID EEPROM
#28 - ID_SC - I2C ID EEPROM
#29 - GPIO05
#30 - Ground
#31 - GPIO06
#32 - GPIO12
#33 - GPIO13
#34 - Ground
#35 - GPIO19
#36 - GPIO16
#37 - GPIO26
#38 - GPIO20
#39 - Ground
#40 - GPIO21


for x in range(1,10):
    gpio.output(x, gpio.HIGH) # HIGH/LOW)
    #arduino.write(b'0')
    x=0
    print(datetime.datetime)
    
gpio.cleanup()