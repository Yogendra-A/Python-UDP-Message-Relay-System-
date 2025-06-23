# Python UDP Message Relay System 🚀

A lightweight local messaging system built using Python's socket programming and the UDP protocol. This project simulates a basic message relay mechanism between a **Client**, a **Server**, and a **GUI Receiver** — ideal for understanding computer networks, sockets, and simple GUI integration.

---

## 🔧 Features

* Real-time message sending using **UDP sockets**
* Local forwarding via a **central server**
* Simple and clean **Tkinter GUI** for message display
* Minimal setup, no external libraries required

---

## 🧱 Project Structure

```plaintext
Python_UDP_Message_Relay/
├── client.py      # Sends messages to the server
├── server.py      # Forwards messages to the receiver
└── receiver.py    # GUI to view received messages
```

---

## 📸 Screenshots

### ✅ Receiver GUI

![receiver](https://github.com/user-attachments/assets/24d85227-3c10-443c-a745-806eec76f56e)<br>

### ✅ Terminal Outputs

* **Client sending a message**

![client](https://github.com/user-attachments/assets/9048063c-95cd-43bd-a703-45caf7f2f3e5)


* **Server forwarding the message**

![server](https://github.com/user-attachments/assets/95aba215-3c27-4d26-9381-d0ede25574dd)


## ⚙️ How to Run

### 1. Start the Receiver GUI

```bash
python3 receiver.py
```

### 2. Start the Server

```bash
python3 server.py
```

### 3. Start the Client

```bash
python3 client.py
```

Now type a message in the client terminal. The server will forward it, and the GUI receiver will display it. 🎉



## 📚 Technologies Used

* **Python 3.12+**
* `socket` module
* `tkinter` (for GUI)

---
