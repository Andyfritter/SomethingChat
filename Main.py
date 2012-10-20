import socket 
print ('Welcome to Andychat v.1.0')
HOST = '192.168.1.109'    # The remote host
PORT = 4            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('fuck blues clues')
data = s.recv(1024)
s.close()
print 'Josh:', repr(data)
