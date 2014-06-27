#!/user/bin/python

import os, os.path

for item in os.listdir('.'):
	if os.path.isfile(item):
		st = os.stat(item)
		print st
