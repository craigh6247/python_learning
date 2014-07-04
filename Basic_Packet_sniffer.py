 #!/user/bin/python

import struct
import socket
import binascii
# please not promisc mode must be enabled to work properly on a network 
# root is required to make raw socket
# setting up sniffer
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
i = 1
while i == 1 :

        pkt = rawSocket.recvfrom(2048)
        # mac portion of poacket
        ethernetHeader = pkt[0][0:14]

        eth_hdr = struct.unpack("6s6s2s", ethernetHeader)

        print "mac host address " + binascii.hexlify(eth_hdr[0])

        print "mac address destenation address " + binascii.hexlify(eth_hdr[1])

        binascii.hexlify(eth_hdr[1])
        # ip address get
        ipHeader = pkt[0][14:34]
        ip_hdr = struct.unpack("!12s4s4s", ipHeader)
        print "host ip : " + socket.inet_ntoa(ip_hdr[1])
        print "Dest ip : " + socket.inet_ntoa(ip_hdr[2])
