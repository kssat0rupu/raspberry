# read_sw.py

import RPi.GPIO as GPIO
from time import sleep

def main():
	GPIO.setmode(GPIO.BCM)
	SW_PIN = 24
	GPIO.setup(SW_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

	try:
		while True:
			sw_status = GPIO.input(SW_PIN)
			if sw_status == GPIO.HIGH: print("Switch status is HIGH")
			else : print("Switch status is LOW")
			sleep(0.5)
	except KeyboardInterrupt:
		pass
	
	GPIO.cleanup()

if __name__ == "__main__":
	main()
