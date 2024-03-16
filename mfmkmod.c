#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/interrupt.h>
#include <linux/gpio/driver.h>
#include <linux/delay.h>

static int fwr(char *path, uint8_t *buf, uint32_t size) {
	struct file *fp;
	int ret = 0;

	fp = filp_open(path, O_RDWR | O_CREAT, 0644);
	loff_t pos = 0;
	ret = kernel_write(fp, buf, size, &pos);
	filp_close(fp, NULL);

	return ret;
}

static int is_right_chip(struct gpio_chip *chip, void *data) {
	if(strcmp(data, chip->label)==0) return 1;
	return 0;
}

int init_module(void) {
	unsigned char *data;

	data = (unsigned char*)kzalloc(4000000, GFP_ATOMIC);

	struct gpio_chip *chip = gpiochip_find("pinctrl-bcm2711", is_right_chip);

	chip->direction_input(chip, 9);
	chip->direction_output(chip, 14, 0); // enable motor
	chip->direction_output(chip, 25, 1); // select side 0 (inverted logic)
	msleep(1000);                        // wait for motor to spin up

	//printk(KERN_INFO "IRQs disabled.\n");
	local_irq_disable();
	for(int i=0; i<4000000; i++)
		data[i] = chip->get(chip, 9);
	local_irq_enable();
	//printk(KERN_INFO "IRQs enabled.\n");

	chip->direction_output(chip, 14, 1); // disable motor
	fwr("/home/pi/prj/pimfm/track0.raw", data, 4000000);
	//printk(KERN_INFO "Wrote file.\n");
	kfree(data);
	return 0;
}

void cleanup_module(void) {
}

MODULE_LICENSE("GPL");
