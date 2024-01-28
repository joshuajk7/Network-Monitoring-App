import socket 


def tcp_server():
    # Create a socket
    server_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket
    server_address = '127.0.0.1'
    server_port = 12345
    server_sock.bind((server_address, server_port))
    
    # Listen for Incoming Connections:
    server_sock.listen(5)
    print("Server is listening for incoming connections...")

    try:
        while True:
            # Accept Connections:
            client_sock, client_address = server_sock.accept()
            print(f"Connection from {client_address}")

            try:
                # Send and Recieve Data:
                # recv(): Recieve data from the client
                message = client_sock.recv(1024)
                print(f"Recieved message: {message.decode()}")

                # sendall(): Send a response back to the client
                response = "Message Received"
                client_sock.sendall(response.encode())
                
            finally:
                # Close Client Connection
                client_sock.close()
                print(f"Connection with {client_address} closed")
        
    except KeyboardInterrupt:
        print("Server is shitting down.")
    
    finally:
        # Close Server Socket:
        server_sock.close()
        print("Server socket closed.")

if __name__ == "__main__":
    tcp_server()
    