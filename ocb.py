# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on Tue Apr 11  2020

@author: Jackson Alessandro dos Santos
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import serial
from datetime import datetime
import time
#import pdb

port=serial.Serial(port='/dev/ttyAMA0',baudrate=9600, timeout=1.0)
eof = "\xff\xff\xff"
Page = 0 #page0 is the norm and page 1 is all black with large #'s for easy reading in the AM

#set screen to undim and on pic 0 and on page 0 when program starts for the first time
port.write("page 1" + eof)

while True:
#formatting date for screen
	x = datetime.now()
	weekday = x.strftime("%a")#Wed
	month = x.strftime("%B")#December
	day = x.strftime("%d")#31
	#year = x.strftime("%Y")#2018
	#yearN = x.strftime("%y")#18
	#monthN = x.strftime("%m")#12 for dec
	#fullDate = (weekday + ", " + month + " " + day + " " + year) 
	fullDate1 = 'page0.Date.txt="'+fullDate+'"'+eof
#formatting time for screen
	hour = x.strftime("%I")#5 - 12 hour time
	min = x.strftime("%M")#21
	#sec = x.strftime("%S")#41
	#AmPm = x.strftime("%p")#AM or PM
	#fullTime = (hour+":"+min+":"+sec+" "+AmPm)
	fullTime1 = 'page0.Time.txt="'+fullTime+'"'+eof
	
	port.write(fullDate1)

