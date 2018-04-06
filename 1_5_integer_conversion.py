#!/usr/bin/python3
# ___________________________________________________________
# Python Network Programming Introduction ITEK - EAAA 2018
# Author Hans Henrik Jeppesen
# Date: 27.03.18 Version 1.0
# Contact: hans@eaaa.dk
# ___________________________________________________________

import socket

def convert_integer():
    while True:
        userInput = int(input('Type in an Integer (0-10000): '))
        if userInput > 10000 or userInput < 0:
            print('The interger you have typed in is not valid, please try again')
        else:
            data = userInput
            break

    # 32 bit conversion Network To Host Long (ntohl) and Host to Network Long (htonl)
    print("Original input: {} => \nLong host byte order: {} \nLong network byte order: {}".format(data, socket.ntohl(data), socket.htonl(data)))

    # 16 bit conversion  Network To Host Short (ntohs) and Host to Network Short (htons)

    print("Original input: {} => \nShort host byte order: {} \nShort network byte order: {}".format(data, socket.ntohs(data), socket.htons(data)))

    if __name__ == '__main__':
        convert_integer()