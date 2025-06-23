# server.py
import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Receiver configuration
RECIVER_HOST = '127.0.0.1'
RECIVER_PORT = 12346

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reciver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server socket
server_socket.bind((HOST, PORT))

print('📡 Server started. Listening for messages...')

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"📨 Received from {client_address}: {message}")

    # Forward the message to the receiver
    reciver_socket.sendto(data, (RECIVER_HOST, RECIVER_PORT))
    print(f"➡️ Forwarded to receiver at {RECIVER_HOST}:{RECIVER_PORT}")
