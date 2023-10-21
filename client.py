import socket

def main():
        server_ip = input("enter ip address ")
        server_port = 1303

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
                client_socket.connect((server_ip, server_port))
                print("Connect with server")

                response = client_socket.recv(1024)
                print(f"Get from server: {response.decode('utf-8')}")

        except ConnectionRefusedError:
                print("Error connection with server. Check ON server and correct IP")
        except Exception as e:
                print(f"Error with connect {str(e)}")
        finally:
                try:
                        client_socket.close()
                except Exception as e:
                        print(f"Error with close socket: {str(e)}")

if __name__ == "__main__":
        main()
