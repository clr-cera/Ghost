import socket               # Import socket module
import data.serverData as serverData
import recognition as rec
import os
import pyaudio as pa

pa.PyAudio()

NAME = 'ghost' #Hi Ghost!

processList = [] #This stores all processes ran by this client

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)          # Create a socket object
s.connect((serverData.HOST, serverData.PORT,0,0))

while True:
    speech = rec.parseCommand()
    name = speech.lower().split()[0]


    if name == NAME:
        s.send(str.encode(speech))

        command = s.recv(1024).decode()
        os.system(command)


s.close()                     # Close the socket when done
