#!/usr/bin/env python3

def bug_trigger(binary_data_cross, x):
	from wand.image import Image
	with Image(filename='/home/net/jo798048/homework2/tests/cross.jpg') as img:
		img.save(filename='/home/net/jo798048/homework2/tests/cross_mutated_test_1.jpg')
		binary_data = open('/home/net/jo798048/homework2/tests/cross_mutated_test_1.jpg', 'wb')
		binary_data.write(binary_data_cross)
		binary_data.close()
		cmd_str="./jpeg2bmp cross_mutated_test_1.jpg cross.bmp"
		import subprocess
		child = subprocess.run(cmd_str, shell=True)
		if child.returncode == 139:
			cmd_str="cp cross_mutated_test_1.jpg /home/net/jo798048/homework2/tests/cross_mutated_" + str(x) + ".jpg"
			child = subprocess.run(cmd_str, shell=True)
			print('TEST NUMBER: ' + str(x))
			return 1
		else:
			cmd_str="rm cross_mutated_test_1.jpg"
			child = subprocess.run(cmd_str, shell=True)
			return 0

def binary_data_modify(binary_data_modification, binary_data_cross, counter):
	import random
	specific_spot = random.randint(0, 807)
	new_data = binary_data_cross[:specific_spot] + binary_data_modification
	add_counter = bug_trigger(new_data, counter)
	counter += add_counter
	return counter

def main():
	binary_data_max = b'\xff'
	binary_data_zero = b'\x00'
	binary_data_mid = b'\x05'
	binary_data_cross = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xe1\x00\x16Exif\x00\x00II*\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xdb\x00C\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xff\xdb\x00C\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xff\xc0\x00\x11\x08\x00\x08\x00\x08\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfe.\xb3\x10*\xfb\xf4\xf1\xfbP5\xab)\x05\xbc\xc0\x8e\x1c(]\xcc|\x84\xfd\xa3V$)\x1e\xe7s\xbdv\xcaO\xc7IQ\x98\xa2\x8a\xfcG5\xcc\x96S<\x04V]\x95f+\x1d\x96\xe1s\x15\xfd\xab\x82\x8e1\xe0V&s_\xd9\xf9{s\xa6\xf0\xd9f\x1f\x93\xfd\x97\x0b\xef\xfb\x1ey\xda\xa4\x93I\x7f\xa9\xde\x1d\xf0D\xbcE\xa1\xc5u\xa7\xc6|}\xc13\xe1.3\xce8.\x7f\xf1\x0fx\x96\xa7\rG\x8a\xe7\x92\xd1\xc0T\x97\x18\xf1\x94V\x1b\x1a\xb3\xbe:\xce\x9e*\xd9\xff\x00\x10/\xaa\xff\x00i}[\x0b)a)\xce\x9c\xa7S\xff\xd9'
	x = 0
	add_counter = 1
	while x != 1650:
		add_counter = binary_data_modify(binary_data_max, binary_data_cross, add_counter)
		add_counter = binary_data_modify(binary_data_mid, binary_data_cross, add_counter)
		add_counter = binary_data_modify(binary_data_zero, binary_data_cross, add_counter)
		x += 1
main()
