import socket
from datetime import datetime

def main():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 1303))
        server_socket.listen(1)

        print("Server is on and waiting connection...")

        while True:
                client_socket, client_address = server_socket.accept()
                print(f"Connect with client {client_address}")

                current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
                client_socket.send(current_time.encode("utf-8"))

                client_socket.close()
                print(f"Connection with {client_address} close")

if __name__ == "__main__":
        main()
