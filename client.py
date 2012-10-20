import socket
from config import *

class Client():
	def __init__(self):
                self.name = raw_input('Enter Name: ')
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((HOST, PORT))
		data = s.recv(1024)
		self.s.close()
		print repr(data)

	def say(self, msg):
                self.s.sendall(self.name + ': ' + msg)
                
