# client.py
import socket

# Server address (unchanged)
HOST = '127.0.0.1'
PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("✉️ Email Client Started")
print("Type your message and press Enter to send. Type 'exit' to quit.\n")

while True:
    # Get user input
    message = input("You: ")

    # Send to the server
    client_socket.sendto(message.encode(), (HOST, PORT))

    if message.lower() == 'exit':
        print("❌ Exiting client.")
        break

client_socket.close()
