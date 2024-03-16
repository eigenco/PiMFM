import RPi.GPIO as GPIO
from time import sleep
from numpy import *
import spidev
import sys

# ground floppy pin 12
MOTEB = 14 # floppy: 16
DIR   = 15 # floppy: 18
STEP  = 18 # floppy: 20
TRK00 = 23 # floppy: 26
RDATA = 9  # floppy: 30
SIDE1 = 25 # floppy: 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTEB, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(TRK00, GPIO.IN)
GPIO.setup(SIDE1, GPIO.OUT)

GPIO.output(SIDE1, 1) # select head 0 (inverted logic)
GPIO.output(MOTEB, 0) # switch on the motor

track = 0

def back():
	global track
	print('Stepping head back to track 0', end='')
	sys.stdout.flush()
	while GPIO.input(TRK00)==1:
		GPIO.output(DIR, 1)
		GPIO.output(STEP, 0)
		GPIO.output(STEP, 1)
		sleep(0.015)
		print('.', end='')
		sys.stdout.flush()
	#print(' ok')
	print('')
	sys.stdout.flush()
	track = 0

def seek_next():
	global track
	GPIO.output(DIR, 0)
	GPIO.output(STEP, 0)
	GPIO.output(STEP, 1)
	track = track + 1

print('Moving head forward', end='')
for x in range(20):
	print('.', end='')
	sys.stdout.flush()
	seek_next()
	sleep(0.25)
print('')
back()

GPIO.output(MOTEB, 1) # switch off the motor
