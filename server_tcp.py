import socket

def aguardar_requisicao(PORTA, LISTEN_HOST="0.0.0.0"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file = open("output.txt", "w")
    try:
        server.bind((LISTEN_HOST, PORTA))
        server.listen(5)
        print("listening...")

        client_socket, address = server.accept()
        print("Received from: " + address[0])

        while True:
            data = client_socket.recv(1024).decode()
            file.write(data)
            server.close()

    except Exception as Error:
        print("Ocorreu um erro.")
        print(Error)

aguardar_requisicao(4466, "0.0.0.0")