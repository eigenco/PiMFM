import sys
from numpy import *

dx = 12.0

src = open('header.dat', 'rb')
data = src.read()
src.close()

f = open('tracks.mfm', 'wb+')

f.seek(0)
f.write(data)

for x in range(1):
	f.seek(65536*x+65536)
	src = open('track' + str(x) + '.mfm', 'rb')
	data = src.read()
	f.write(data)

f.close()
