import socket

mi_socket = socket.socket()

mi_socket.connect( ('localhost', 8000) )

mi_socket.send("su ip y puerto fueron enviados a una persona anonima!")

respuesta = mi_socket.recv(1024)

print respuesta

mi_socket.close()
