import serial
import time

# Open a serial connection
s = serial.Serial("/dev/ttyACM0", 115200)

# print("Enter a voltage value between 0 and 10000 mV. Type 'exit' to quit.")
print("Reading data from Raspberry Pi Pico...")

# Loop to wait for user input
while True:
    if s.in_waiting > 0:
        # Read the line from the serial port
        lux_value = s.readline().decode().strip()
        # Print the received data
        print(f"Received data: {lux_value}")