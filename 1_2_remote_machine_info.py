#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________
import socket

def get_remote_machine_info(domain):
    remote_host = domain
    try:
        print ("IP address of {} {}".format(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("{} {}".format(remote_host, err_msg))

while True:
    userInput = input('Enter the domain you want to get IP of (enter exit() to quit): ')
    if userInput.lower() == 'exit()':
        # clears the console on raspberry pi
        print("\033c")
        print('Have a nice day')
        print('\n')
        break
    else:
        get_remote_machine_info(userInput)