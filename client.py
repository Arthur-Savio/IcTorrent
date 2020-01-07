import socket             

s = socket.socket()             
host = socket.gethostname()     
port = 60000                    

s.connect((host, port))

with open('received-files/file.jpg', 'wb') as f:
    print('file opened')
    
    while True:
        data = s.recv(1024)

        print('receiving data...')
        if not data:
            break
        
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')