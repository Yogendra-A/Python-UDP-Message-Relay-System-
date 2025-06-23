import socket
import tkinter as tk

# Receiver configuration
HOST = '127.0.0.1'
PORT = 12346

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind((HOST, PORT))
receiver_socket.setblocking(0)

root = tk.Tk()
root.title("Email Receiver")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Received Messages:")
label.pack()

text_box = tk.Text(frame, height=10, width=50)
text_box.pack()

def receive_message():
    try:
        data, server_address = receiver_socket.recvfrom(1024)
        message = f"From {server_address}: {data.decode()}\n"
        text_box.insert(tk.END, message)
    except socket.error:
        pass

receive_button = tk.Button(frame, text="Receive", command=receive_message)
receive_button.pack()

root.mainloop()
