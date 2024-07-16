from machine import I2C, Pin
import time

# Address and command constants
TSL2561_ADDR = 0x29  # Detected address
CMD = 0x80
WORD = 0x20
POWER_UP = 0x03
POWER_DOWN = 0x00
CONTROL = 0x00
TIMING = 0x01
CH0_LOW = 0x0C
CH1_LOW = 0x0E
GAIN_16X = 0x10
INTEGRATIONTIME_402MS = 0x02

class TSL2561:
    def __init__(self, i2c, addr=TSL2561_ADDR):
        self.i2c = i2c
        self.addr = addr
        self.power_up()

    def power_up(self):
        try:
            self.i2c.writeto_mem(self.addr, CMD | CONTROL, bytearray([POWER_UP]))
            print("Sensor powered up successfully")
        except OSError as e:
            print("Failed to power up sensor:", e)
            raise

    def power_down(self):
        try:
            self.i2c.writeto_mem(self.addr, CMD | CONTROL, bytearray([POWER_DOWN]))
            print("Sensor powered down successfully")
        except OSError as e:
            print("Failed to power down sensor:", e)
            raise

    def set_gain_and_timing(self, gain, timing):
        try:
            self.i2c.writeto_mem(self.addr, CMD | TIMING, bytearray([gain | timing]))
            print("Gain and timing set successfully")
        except OSError as e:
            print("Failed to set gain and timing:", e)
            raise

    def read_word(self, reg):
        try:
            data = self.i2c.readfrom_mem(self.addr, CMD | WORD | reg, 2)
            return data[1] << 8 | data[0]
        except OSError as e:
            print("Failed to read word:", e)
            raise

    def read_lux(self):
        ch0 = self.read_word(CH0_LOW)
        ch1 = self.read_word(CH1_LOW)
        if ch0 == 0:
            return None
        ratio = ch1 / ch0
        if ratio <= 0.5:
            lux = 0.0304 * ch0 - 0.062 * ch0 * (ratio ** 1.4)
        elif ratio <= 0.61:
            lux = 0.0224 * ch0 - 0.031 * ch1
        elif ratio <= 0.80:
            lux = 0.0128 * ch0 - 0.0153 * ch1
        elif ratio <= 1.30:
            lux = 0.00146 * ch0 - 0.00112 * ch1
        else:
            lux = 0
        return lux


