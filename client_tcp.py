import socket

def enviar_requisicao(HOST, PORTA, MENSAGEM):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORTA))
        client.send(MENSAGEM.encode('utf-8'))
        pacotes_recebidos = client.recv(1024).decode()
        print(pacotes_recebidos)
    except:
        print("Ocorreu um erro.")

enviar_requisicao("google.com", 80, "GET / HTTP/3\nHost: www.google.com\n\n\n")