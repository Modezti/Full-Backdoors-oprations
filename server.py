import socket
import struct

ip = "localhost"
port = 12345
bufsize = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(1)
print("server listen...")

client, addresse = server.accept()
print(f"connection de {addresse}")

def send_message(client_socket, message):
    longueur_message = len(message.encode())
    client_socket.sendall(struct.pack("!I", longueur_message))
    client_socket.sendall(message.encode())

def receive_message(client_socket):
    get_data_len = client_socket.recv(4)
    message_len = struct.unpack("!I", get_data_len)[0]
    print("length message client is: ", message_len)

    # envoyer la longeur du message    message = b""
    while len(message) < message_len:
        chunk = message_len - len(message)
        chunk_size = bufsize if chunk > bufsize else chunk
        data = client_socket.recv(chunk_size)
        message += data
    return message.decode()

while True:
    command = input("shell>> ")
    send_message(client, command)
    if command == "":
        continue

    elif command.startswith("cd"):
        reponse = receive_message(client)
        print(reponse)

    else:
        reponse = receive_message(client)
        print(reponse)

client.close()
server.close()
