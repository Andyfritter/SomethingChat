import socket
from config import *

class Server():
	def __init__(self):
		# Echo server program
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.s.bind(('', PORT))
		self.s.listen(1)

		conn, addr = self.s.accept()
		print 'Connected by', addr
		conn.close()

	def read_loop(self):
		while True:
		    data = conn.recv(1024)
		    if not data: break

		    self.say(data)

	def say(self, msg):
		self.conn.sendall(msg);