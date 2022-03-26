# adt7410_i2c.py

import smbus
from time import sleep
import RPi.GPIO as GPIO

def get_temp_ADT7410_i2c(i2c, address):
	block = i2c.read_i2c_block_data(address, 0x00, 12)
	data = (block[0] << 8 | block[1]) >> 3
	if data >= 4096: data -= 8192
	temp = data/16.0
#print(" |{:x}".format(block[0]),"|{:x}".format(block[1]),end="")
	return temp

def main():
	i2c = smbus.SMBus(1)
	address = 0x48

	try:
		while True:
			temp = get_temp_ADT7410_i2c(i2c,address)
			#print("| Temp = {:6.2f}".format(temp))
			print(" Temp = {:6.2f}".format(temp))
			sleep(5)

	except KeyboardInterrupt:
		pass

	GPIO.cleanup()

if __name__ == "__main__":
	main()
