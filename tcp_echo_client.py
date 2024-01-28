import socket


def tcp_client():
    # Create a Socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify Server Address and Port
    server_address = '127.0.0.1'
    server_port = 12345

    try:
        # Establish a Connection:
        sock.connect((server_address, server_port))

        # Send and Recieve Data:
        message = 'Hello, Server!'
        print(f"Sending: {message}")
        sock.sendall(message.encode())

        response = sock.recv(1024)
        print(f"Recieved: {response.decode()}")

    finally: 
        # Close the Connection:
        sock.close()

if __name__ == "__main__":
    tcp_client()
