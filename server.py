import socket

s = socket.socket()
host = "127.0.0.1"
port = 8080
s.bind((host, port))

s.listen(1)
print("Waiting for connection...")
conn, addr = s.accept()
print(f"Connected to {addr}")

# Send a welcome message to the client
conn.send(b"Welcome to the server!")

while True:
    # Server sends a message
    msg = input("server>> ")
    conn.send(msg.encode())
    print(f"Sent: {msg}")

    # Server receives a message
    msg = conn.recv(1024).decode()
    print(f"client>> {msg}")
