import serial
import serial.tools.list_ports
import time

def find_pico_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Board CDC" in port.description:  # Adjust this string to match your device description
            return port.device
    return None

# Find the Pico port
pico_port = find_pico_port()
if not pico_port:
    print("Raspberry Pi Pico not found. Please check the connection.")
    exit()

# Open a serial connection
s = serial.Serial(pico_port, 115200)

print("Reading data from Raspberry Pi Pico...")

# Loop to read data from Pico
while True:
    if s.in_waiting > 0:
        # Read the line from the serial port
        lux_value = s.readline().decode().strip()
        # Print the received data
        print(f"Received data: {lux_value}")
