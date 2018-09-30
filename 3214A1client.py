import socket
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect
host = input('Please input host IP: ')
port = int(input('Port: '))
  
# connect to the server on local computer 
s.connect((host, port)) 

client_input = []
prompt = []
prompt.append('Please input an integer: \n')
prompt.append('Now input a string: \n')
# input data to send to server
for i in range(0, 2):
    client_input.append(input(prompt[i]))
    s.sendall(client_input[i].encode())
# receive n lines from server and write into file
filename = 'received.out'
for i in range(0, int(client_input[0])):
    result = s.recv(1024).decode()
    with open(filename, "a") as f:
        f.write(result)
        f.close()
# close connection with server
s.close()