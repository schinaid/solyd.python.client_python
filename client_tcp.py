import socket

def enviar_requisicao(HOST, PORTA, MENSAGEM):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORTA))
        client.send(MENSAGEM.encode('utf-8'))
        pacotes_recebidos = client.recv(1024).decode()
        print(pacotes_recebidos)
    except Exception as Error:
        print("Ocorreu um erro.")
        print(Error)

enviar_requisicao("127.0.0.1", 4466, "estou guadrando isso")