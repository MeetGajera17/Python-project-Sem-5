import socket
print("hello")
s = socket.socket()
host = "127.0.0.1"
port = 8080

try:
    s.connect((host, port))
    print("Connected to the server.")
except ConnectionRefusedError:
    print("Connection refused. Is the server running?")
    exit()

# Receive the initial message from the server
msg = s.recv(1024).decode()
print(f"server>> {msg}")

while True:
    # Client receives a message
    msg = s.recv(1024).decode()
    print(f"server>> {msg}")

    # Client sends a message
    msg = input("client>> ")
    s.send(msg.encode())
    print(f"Sent: {msg}")
