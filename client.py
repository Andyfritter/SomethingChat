import socket
from config import *

class Client():
	def __init__(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
		s.sendall('fuck blues clues')
		data = s.recv(1024)
		s.close()
		print 'Josh:', repr(data)