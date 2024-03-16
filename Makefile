obj-m += mfmkmod.o
CFLAGS = -O0

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	rm -f *.raw
	rm -f *.mfm
	rm *.mod.c
	rm *.order
	rm *.symvers
	rm *.mod
	rm *.ko
	rm *.o
