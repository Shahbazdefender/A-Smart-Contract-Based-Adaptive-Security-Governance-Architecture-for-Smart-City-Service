import socket

# Create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
serverAddress = ('localhost', 5001)
serverSocket.bind(serverAddress)

# Listen for incoming connections
serverSocket.listen(1)
print('SDN Server of Disaster Managment to connect...')

while True:
    # Accept a new connection
    print("Disaster Managment Application Started............")
    clientSocket, clientAddress = serverSocket.accept()
    print('Client connected:', clientAddress)

    # Receive a message from the client and print it to the console
    message = clientSocket.recv(1024).decode()
    print('Received message from client:', message)

    # Send a response back to the client
    response = 'Hello from Python server!'
    clientSocket.send(response.encode())

    # Close the client socket
    clientSocket.close()
