import socket

mi_socket = socket.socket()

mi_socket.bind( ('localhost', 8000) )

mi_socket.listen (5)

while True:

conexion, addr = mi_socket.accept()

print "victima a ejecutado el script!"

print addr

conexion.send("hola, soy zxfeh ")

conexion.close() 
