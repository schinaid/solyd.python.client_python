import socket

def aguardar_requisicao(PORTA, LISTEN_HOST="0.0.0.0"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((LISTEN_HOST, PORTA))
        server.listen(5)
        print("listening...")

        client_socket, address = server.accept()
        print("Received from: " + address[0])

        while True:
            data = client_socket.recv(1024).decode()
            if data == "senhaSecreta\n":
                client_socket.send(b"mensagem secreta")
            print(data)
            client_socket.send(input("Digite a mensagem: ").encode())

    except Exception as Error:
        print("Ocorreu um erro.")
        print(Error)
        server.close()

aguardar_requisicao(4433, "0.0.0.0")