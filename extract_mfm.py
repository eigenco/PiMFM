import sys
from numpy import *

dx = 12.0

f = open('track0.raw', 'rb')
data = fromfile(f, dtype=int8)
f.close()

f = open('track0.mfm', 'wb')

###
# record transitions and clock accordingly in order to
# acquire the correct number of zero bits

bits = [0]*len(data)
px = 0
for x in range(len(data)-1):
	if data[x]<data[x+1]:
		bits[x + 1] = 2
		bits[round(x - 0.5*dx)] = 1
		if x - px > round(2.5 * dx): bits[round(x - 1.5 * dx)] = 1
		if x - px > round(3.5 * dx): bits[round(x - 2.5 * dx)] = 1
		px = x + 1
		sys.stdout.flush()
	else:
		True
	if x % 100000 == 0:
		print('.', end='')
		sys.stdout.flush()
print('')
sys.stdout.flush()

###
# extract MFM data accordingly

value = 0
value_index = 0
for x in range(len(bits)):
	if bits[x] == 1:
		value_index = value_index + 1
		if value_index == 8:
			f.write(bytearray([value]))
			value_index = 0
			value = 0
	if bits[x] == 2:
		if value_index == 0: value = value | 128
		if value_index == 1: value = value | 64
		if value_index == 2: value = value | 32
		if value_index == 3: value = value | 16
		if value_index == 4: value = value | 8
		if value_index == 5: value = value | 4
		if value_index == 6: value = value | 2
		if value_index == 7: value = value | 1
		value_index = value_index + 1
		if value_index == 8:
			f.write(bytearray([value]))
			value_index = 0
			value = 0
	if x % 100000 == 0:
		print('.', end='')
		sys.stdout.flush()
print('')
f.close()
