<<<<<<< HEAD
print((1/2) * 0.8 * ((1/(1^2)) + ( 2 * ( (1/(1.8^2)) + (1/(2.6^2)) + (1/(3.4^2)) + (1/(4.2^2)) ) ) + (1/25) ))
=======
from zipfile import ZipFile

for i in range(100, 1000):
	with ZipFile('/tmp/alien-zip-2092.zip') as zf:
		try:
			zf.extractall(pwd=str(i))
			print i
			break
		except IOError:
			print i
			pass


for i in possiblePasswordList:
	try:
		zf = ZipFile.open('/tmp/alien-sample-42.zip', 'r', pwd=i)
		print i
		zf.extractall()
		break
	except:
		pass




import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("localhost", 10000) )
s.send("GET_KEY")
recv = s.recv(1024)
print recv

recv = recv[::-1]

print recv

s.send(recv)

s.close



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("localhost", 10000) )
s.send("/tmp")
s.send("all")
recv = s.recv(1024)
print recv
s.close




import magic


>>>>>>> a75b423a789e93b934a368193b1cf255a3254f63
