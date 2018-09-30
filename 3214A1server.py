# -*- coding: utf-8 -*-
import socket                

try:
    s = socket.socket()          
    print ("Socket successfully created")
    port = int(input('Port: '))
    
    s.bind(('', port))
    print ("socket binded to %s"%(port)) 
      
    s.listen(5)      
    print ("socket is listening")
except Exception as E:
    print (E)



c, addr = s.accept()      
print ('Got connection from', addr)
received_data = []
#### wait for integer n and string 
for i in range(0, 2):
    received_data.append(c.recv(1024).decode())
received_data[0] = int(received_data[0])

#### send n lines of received strng
for i in range(0, received_data[0]):
    c.sendall(received_data[1].encode())
#### tell client that server is done sending
print ('Connection terminated')
c.close()

   