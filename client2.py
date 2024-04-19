import socket

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Client 2: Enter your message: ")
        client.send(message.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")
        print("Server:", response)

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5555
    start_client(HOST, PORT)
