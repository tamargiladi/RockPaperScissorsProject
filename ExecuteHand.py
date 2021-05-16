# Importing Libraries
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
#
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value

t=0
while (t<5):
    value = write_read("p")
    print(value) # printing the value
    t+=1

'''
def doRock():
    value = write_read("r")
    print(value)  # printing the value


def doScissors():
    value = write_read("s")
    print(value)  # printing the value


def doPaper():
    value = write_read("p")
    print(value)  # printing the value
'''






