import select
import sys
import time
from DfrobotGP8403 import *
import utime
from TSL2561 import *
from machine import I2C, Pin

def store():
    # Store data in the chip
    DAC.store()

# Set up the poll object
poll_obj = select.poll()
poll_obj.register(sys.stdin, 1)

# Set up i2c port
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

#initialize sensors
sensor = TSL2561(i2c)
DAC = DfrobotGP8403(0x5F, 17, 16, 400000, True)


sensor.set_gain_and_timing(GAIN_16X, INTEGRATIONTIME_402MS)
DAC.set_dac_out_range(OUTPUT_RANGE_10V)


if __name__ == "__main__":
    while True:
        lux = sensor.read_lux()
        print(f"{lux}")
        time.sleep(1)
        poll_results = poll_obj.poll(1)
        if poll_results:
            # Read the data from stdin (read data coming from PC)
            data = sys.stdin.readline().strip()
            
            try:
                # Convert the data to an integer
                voltage = int(data)
                
                # Set the DAC output voltage
                DAC.set_dac_out_voltage(voltage, 1)
            except ValueError:
                sys.stdout.write("Invalid data received. Not an integer.\r")
        
            continue
