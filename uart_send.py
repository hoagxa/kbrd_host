#!/usr/bin/python3

import time
import serial

ser = serial.Serial(
	port = '/dev/ttyAMA0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

print("Raspberry's sending : ")

try:
    while 1:
    	ser.write(b'Hello Adruino!')
    	ser.flush()
    	print("Hello Arduino!")
    	time.sleep(1.1)
except KeyboardInterrupt:
	ser.close()