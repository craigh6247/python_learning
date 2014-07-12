#!/user/bin/python

import binascii
import struct

filename = raw_input("please type in the file you would like to view: \n")
with open(filename, 'rb') as f :
	content = f.read()
hex = binascii.hexlify(content)
hex_list = list(hex)
print(hex_list[:8])
