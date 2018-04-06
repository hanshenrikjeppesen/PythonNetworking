#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 53]:
        print("Port: {} => Service name: {}".format(port, socket.getservbyport(port, protocolname)))

if __name__ == '__main__':
    find_service_name()