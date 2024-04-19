import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                print(f"[{client_address}] disconnected.")
                break
            print(f"[{client_address}] {message}")
            broadcast_message(message, client_socket)
        except ConnectionResetError:
            print(f"[{client_address}] forcibly disconnected.")
            break

    client_socket.close()

def broadcast_message(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(f"{message}\n".encode("utf-8"))  # Include newline character
            except socket.error:
                # Remove disconnected client
                clients.remove(client_socket)

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    clients = []  # List to keep track of connected clients
    HOST = "127.0.0.1"
    PORT = 5555
    start_server(HOST, PORT)
