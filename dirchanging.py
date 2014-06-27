#!/user/bin/python

import os

os.getcwd()

os.chdir('a')

for item in os.listdir('.'):
	if os.path.isfile(item):
		print item
	elif os.path.isdir(item):
		print item
		change = raw_input("""would you like to change to a diffrent directory
?""")

		if change == 'y':
			os.chdir(item)
			for items in os.listdir('.'):
				os.path.isfile(items)
				print items
