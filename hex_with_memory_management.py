#!/user/bin/python

import binascii
import struct
import os
import threading
import queue
import time

class WorkerThread(threading.Thread) :
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self) :
        print "in work thread" 
        while True :
            counter = self.queue.get()
            curen_dir = os.getcwd()
            print curen_dir
            new_dir = raw_input("""please select a directory to change to please incude full path """)
            new_dir.strip()
            
            fd = os.open(new_dir, os.O_RDONLY)
            os.fchdir(fd)
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
            self.queue.task_done()


for i in range (10) :
	print "creating worker thread :%d"%i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "worker thread %d created"%i
for j in range(10) :
    queue.put(j)
queue.join()
  
