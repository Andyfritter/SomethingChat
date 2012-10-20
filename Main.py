import socket 
import client, server
from config import *

print ('Welcome to Andychat v.1.0')

while True:
	client_msg = raw_input("Would you like to run as a client? (y/n) ")
	if client_msg == "y":
		conn = client.Client()
		break
	else:
		server_msg = raw_input("Would you like to run a server? (y/n) ")
		if server_msg == "y":
			conn = server.Server()
			break