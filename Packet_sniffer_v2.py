 #!/user/bin/python

import struct
import socket
import binascii
import os
# setting up sniffer

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

i = 1
doc = open('network_data.txt', 'a')
while i == 1 :

	pkt = rawSocket.recvfrom(2048)
	# mac portion of poacket
	ethernetHeader = pkt[0][0:14]
	eth_hdr = struct.unpack("6s6s2s", ethernetHeader)
	doc.write("Mac host address {:s} \n".format(binascii.hexlify(eth_hdr[0])))
	#doc.write(str("mac host address " + binascii.hexlify(eth_hdr[0]))
	doc.write("mac destenation address {:s} \n".format(binascii.hexlify(eth_hdr[1])))
	#doc.write(str("mac address destenation address: ")  
	binascii.hexlify(eth_hdr[1])
	binascii.hexlify(eth_hdr[1])

	# ip address get
	ipHeader = pkt[0][14:34]
	ip_hdr = struct.unpack("!12s4s4s", ipHeader)
	doc.write("host ip : {:s}\n".format(socket.inet_ntoa(ip_hdr[1])))
	print "this is working"
	#print "Dest ip : " + socket.inet_ntoa(ip_hdr[2])
