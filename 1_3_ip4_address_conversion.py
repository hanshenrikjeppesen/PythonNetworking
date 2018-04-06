#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________

import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.3.14','192.168.1.1']:

        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        print("IP Address: {} => Packed: {}, Unpacked: {}".format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

if __name__ == '__main__':
    convert_ip4_address()

'''
Why?

When you deal with low-level network functions the normal string notation or dotted decimal notation  of IP addresses
are not very useful. They need to be converted to the packed 32-bit binary format.

HOW IT WORKS

The three IPv4 addresses have been converted from a string to a 32-bit packed format using a for-in statement. 
Additionally, the python function hexlify is called from the module that we also import binascii. 
This is helping us repreent the binary data in a hexadecimal format
'''
