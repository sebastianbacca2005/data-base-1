import serial
import time
import os 

os.system("clear")
arduino_port= "COMX" #Replace wirh your port 
baud_rate= 9600
ser=serial.Serial(
    arduino_port,
    baud_rate,
    timeout=1
)
time.sleep(2)