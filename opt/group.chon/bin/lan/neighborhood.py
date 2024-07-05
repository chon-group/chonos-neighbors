import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("255.255.255.255", 3269))

while True:
     data, addr = sock.recvfrom(256) # buffer size is 256 bytes
     binary_file =  open("/dev/shm/.embedMAS/neighbors/list", "ab")
     binary_file.write(data)
     binary_file.write(str.encode("\n"))
     binary_file.close()
