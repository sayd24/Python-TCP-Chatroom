import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, _client_sender):
    for client in clients:
        if client != _client_sender:
            try:
                client.send(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception("Client terputus")
            
            print(f"[CHAT LOG] {message.decode('utf-8')}")
            
            broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                print(f"[DISCONNECT] {nickname} keluar dari jaringan.")
                broadcast(f"--- {nickname} telah meninggalkan obrolan ---".encode('utf-8'), server)
                nicknames.remove(nickname)
            break

def receive_connections():
    print(f"[START] Server berjalan di {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"[CONNECT] Terhubung dengan {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        clients.append(client)

        print(f"[NICKNAME] Client mendaftar dengan nama: {nickname}")
        broadcast(f"--- {nickname} bergabung dalam obrolan! ---".encode('utf-8'), server)
        client.send("Berhasil terhubung ke server!\n".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()