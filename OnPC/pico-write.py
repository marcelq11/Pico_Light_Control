import serial
import time

# Open a serial connection
s = serial.Serial("/dev/ttyACM0", 115200)

# print("Enter a voltage value between 0 and 10000 mV. Type 'exit' to quit.")
print("Reading data from Raspberry Pi Pico...")

# Loop to wait for user input
while True:
    command = input("Enter voltage (0-10000 mV): ").strip()

    if command.lower() == "exit":
        print("Exiting program.")
        break

    try:
        voltage = int(command)
        if 0 <= voltage <= 10000:
            s.write(f"{voltage}\n".encode())
            print(f"Sent voltage: {voltage} mV")
        else:
            print("Invalid voltage. Please enter a value between 0 and 10000 mV.")
    except ValueError:
        print("Invalid input. Please enter an integer value between 0 and 10000 mV.")

