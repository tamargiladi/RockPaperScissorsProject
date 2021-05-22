# Importing Libraries
import serial
import time

TIME = 8
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def doRock():
    t = 0
    while (t <TIME):
        value = write_read("r")
        print(value)  # printing the value
        t += 1

def doScissors():
    t = 0
    while (t < TIME):
        value = write_read("s")
        print(value)  # printing the value
        t += 1

def doPaper():
    t = 0
    while (t <TIME):
        value = write_read("p")
        print(value)  # printing the value
        t += 1



