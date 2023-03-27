import socket

UDP_IP = "0.0.0.0"
# UDP_IP = "192.168.1.20"
UDP_PORT = 3333

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)