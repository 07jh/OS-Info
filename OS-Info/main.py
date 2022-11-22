#IMPORTING
import os
import socket
import platform

#GETTING THE USER
print('Currently logged in as "' + os.getlogin() + '"')

#GETTING THE DEVICENAME
print('Currently on "' + socket.gethostname() + '"')

#GETTING THE IP
print('My IP is "' + socket.gethostbyname(socket.gethostname()) + '"')

#GETTING THE OS
print('Using "' + platform.platform() + '"')

