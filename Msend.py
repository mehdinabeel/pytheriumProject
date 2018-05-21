import socket
import sys
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

        # Receive the data in small chunks and retransmit it
while True:
   # establish a connection
   clientsocket,addr = sock.accept()

   print("Got a connection from %s" % str(addr))
   #rand = random.randint(1,100)
   #msg = str(rand)
   #clientsocket.send(msg.encode('ascii'))
   list = (str(random.randint(250,260)),str(random.randint(150,170)),str(random.randint(280,300)))
   s = "-"
   code = s.join(list)
   p =" "
   join = ("Data:",code)
   stream = p.join(join)

   clientsocket.send(stream.encode())
   clientsocket.close()
