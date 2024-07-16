import serial
import time

# open a serial connection
s = serial.Serial("/dev/ttyACM0", 115200)

# blink the led
while True:
    s.write(b"on\n")
    time.sleep(1)
    s.write(b"of\n")
    time.sleep(1)