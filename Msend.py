import socket
import sys
import random
#for Machine
from cpppo.server.enip import client

host = "152.1.58.247" # Or, simply use an IP address, eg: 192.168.1.2
tags = [ "s[0]","Program:MainProgram.C1.ACC" ]
timeout = 1.0


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
   #machine data
   try:
       with client.connector( host=host, timeout=timeout) as conn:
           for index,descr,op,reply,status,value in conn.pipeline(
                   operations=client.parse_operations( tags ), depth=1 ):
               if (index == 0):
                   A = value[0] #machine ID
               if (index == 1):
                   B = value[0] #machine Count
   except OSError as err:
       A = "8"
   except ValueError:
       print("Could not convert data to an integer.")
   except:
       print("Unexpected error:", sys.exc_info()[0])
       raise

   if(A == "X"):
       stream =""
       print(stream)
   if(A == 1882604571):
       stream = "5"
       print(stream)

   clientsocket.send(stream.encode())
   clientsocket.close()
