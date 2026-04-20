import socket

def enviar_requisicao(HOST, PORTA):
    try:
        while True:
            mensagagem = input("Mensagem: ") + "\n"
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(mensagagem.encode('utf-8'), (HOST, PORTA))
            data, sender = client.recvfrom(1024)
            print(sender[0] + ": " + data.decode())
            if data.decode() == "sair\n" or mensagagem == "sair\n":
                break
        client.close()
    except Exception as error:
        print("Ocorreu um erro.")
        print(error)

enviar_requisicao("192.168.18.41", 4433)