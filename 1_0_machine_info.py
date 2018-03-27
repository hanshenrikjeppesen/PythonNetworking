#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________

# Import module
import socket

# Making a function that gives us the hostname and the ip-address
def print_machine_info():
    # we have two variables that we assign values to
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    # print the variables using the .format notation you can learn more here: https://do.co/2G9uI7G
    print ("Host name: {} and the IP address of this device is: {}".format(host_name, ip_address))

print_machine_info()