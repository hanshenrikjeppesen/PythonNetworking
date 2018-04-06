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
    for port in [80, 25, 53, 8080, 22]:
        print("Port: {} => Service name: {}".format(port, socket.getservbyport(port, protocolname)))

if __name__ == '__main__':
    find_service_name()

'''
Why?

It can be helpful to determine what network services run on which ports using either the TCP or the UDP protocol. 
We can do that by using getservbyport() socket class function from the socket library


'''