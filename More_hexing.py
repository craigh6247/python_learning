#!/user/bin/python

import binascii
import struct
import os

os.getcwd()
#new_dir = raw_input("please select a directory to change to")
#os.chdir(new_dir)
save_file = raw_input(""""please type a file that you would like to save the hex to including file type""" )
doc = open(save_file, 'a')
filename = raw_input("""please type in the file you would like to view:(if all plese type *) \n""")
if filename == "*" :
	for item in os.listdir('.'):
		if os.path.isfile(item):
			file_name = open(item, 'rb')
			with file_name  as f :
			        content = f.read()
			hex = binascii.hexlify(content)
			hex_list = list(hex)
			writing = (hex_list[:8])
			doc.write("This is a file header for %s %s\n"  % (file_name.name, writing ))
else :
	file_name = open(filename, 'rb')
	with file_name  as f :
		content = f.read()
	hex = binascii.hexlify(content)
	hex_list = list(hex)
	writing = (hex_list[:8])
	
	doc.write("this is the file header for %s %s"  % (file_name, writing))

