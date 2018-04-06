#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________

import socket

def convert_integer(data):
    print('\n')

    # 32 bit conversion Network To Host Long (ntohl) and Host to Network Long (htonl)
    print("Original input: {} => \n\033[1;32;40mLong host byte order: {} \n\033[1;34;40mLong network byte order: {}".format(data, socket.ntohl(data), socket.htonl(data)))

    # separation of output for better readable
    print('\n')
    print('\033[1;37;40m' + 20 * "#")
    print('\n')
    # 16 bit conversion  Network To Host Short (ntohs) and Host to Network Short (htons)
    print("Original input: {} => \n\033[1;32;40mShort host byte order: {} \n\033[1;34;40mShort network byte order: {}".format(data, socket.ntohs(data), socket.htons(data)))

while True:
    userInput = (input('\033[1;37;40mType in an Integer (0-10000) or "exit()" to quit: '))
    if userInput.isalpha():
        if userInput == 'exit()':
            print('Have a nice day')
            break
        else:
            print('alpha is not allowed, please try again')
    elif int(userInput) > 10000 or int(userInput) < 0:
        print('The integer you have typed in is not valid, please try again')
    else:
        data = int(userInput)
        convert_integer(data)



'''
WHY?
When we design low-level network applications, it may be necessary to handle the low-level data transmission over the
wire between two machines. This operation requires some sort of conversion of data from the native
host operating system to the network format and vice versa. This is because each one has its 
own specific representation of data

'''