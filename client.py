import socket
from config import *

class Client():
	def __init__(self):
                self.name = raw_input('Enter Name: ')
                try: self.host = HOST
                except: self.host = raw_input('Enter Host\'s IP: ')
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.host, PORT))
                data = s.recv(1024)
                self.s.close()
		print repr(data)

	def say(self, msg):
                self.s.sendall(self.name + ': ' + msg)
                

        
