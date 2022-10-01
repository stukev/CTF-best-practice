import socket

# this script connects to a server/port and answers "questions" based upon queries
# in this example we had to answer YES if the color green was present and NO if it wasn't
# this needs to be repeated until we get the flag (hence the while 1 loop)
# adapt to your needs!

HOST = '152.96.7.28'
PORT = 777
CHECK = '\x1b[92m' #green text

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    s.send('\n'.encode()) # send enter, remove this if not needed for your ctf!
    data = s.recv(1024)
    print('Received', repr(data))
    while 1:
        if CHECK.encode() in data:
            s.send('YES'.encode())
            data = s.recv(1024)
            print('Received', repr(data))
        else:
            s.send('NO'.encode())
            data = s.recv(1024)
            print('Received', repr(data))

print('Received', repr(data))
