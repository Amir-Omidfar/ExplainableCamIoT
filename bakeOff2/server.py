import socket
import time 

channel = input('Channel:')
########################
time.sleep(2)
tServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tServer.bind(('192.168.1.67', int(channel)))
tServer.listen(0)
connect,addr = tServer.accept()
###############while loop for displaying the data

try:
	while True:
		data=connect.recv(1024)
		print(str(data))

finally:
        tServer.close()

