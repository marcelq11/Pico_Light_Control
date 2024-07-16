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

# Loop to wait for user input
while True:
    command = input("Enter voltage (0-10000 mV) or 'on'/'off' to control the relay: ").strip()

    if command.lower() == "exit":
        print("Exiting program.")
        break

    if command.lower() == "on" or command.lower() == "off":
        s.write(f"{command}\n".encode())
        print(f"Sent command: {command}")
    else:
        try:
            voltage = int(command)
            if 0 <= voltage <= 10000:
                s.write(f"{voltage}\n".encode())
                print(f"Sent voltage: {voltage} mV")
            else:
                print("Invalid voltage. Please enter a value between 0 and 10000 mV.")
        except ValueError:
            print("Invalid input. Please enter an integer value between 0 and 10000 mV or 'on'/'off' to control the relay.")
