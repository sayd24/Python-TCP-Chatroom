import socket
import threading
import sys

nickname = input("Masukkan nickname kamu: ")

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Gagal terhubung. Pastikan server sudah dinyalakan!")
    sys.exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Koneksi ke server terputus!")
            client.close()
            break

def write_messages():
    while True:
        try:
            user_input = input("")
            if user_input.strip() != "":
                message = f"{nickname}: {user_input}"
                client.send(message.encode('utf-8'))
        except:
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_messages()