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
gpio.setmode(gpio.BCM)   # Contagem do PINOUT, no. GPIO (BCM/BOARD)
gpio.setup(x, gpio.IN)

for x in range(1,10):
    gpio.output(x, gpio.HIGH) # HIGH/LOW)
    #arduino.write(b'0')
    x=0
    print(datetime.datetime)
    
gpio.cleanup()