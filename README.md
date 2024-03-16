This is code for demostrating reading of raw flux data from old floppy drivers using nothing but Raspberry Pi with linux.

1. You should add isolcpus=1,2,3 to your /boot/cmdline.txt
2. You should edit mfmkmod.c for desired path

# floppy pin 12 should be grounded (this enables the drive)
MOTEB = 14 # floppy: 16
DIR   = 15 # floppy: 18
STEP  = 18 # floppy: 20
TRK00 = 23 # floppy: 26
RDATA = 9  # floppy: 30
SIDE1 = 25 # floppy: 32
