import socket
import time 

channel = 4040
########################
time.sleep(2)
tServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tServer.bind(('192.168.1.67', int(channel)))
tServer.listen(0)
connect,addr = tServer.accept()
###############while loop for displaying the data
def connection():
	active=True
	try:
		while active:
			t=2+2
			
			

	finally:
	        tServer.close()

