import paramiko
import os
from dotenv import load_dotenv

# 1. Carrega as configurações do arquivo .env
load_dotenv()

#Variaveis de ambiente
HOST = os.getenv("SSH_HOST")
USER = os.getenv("SSH_USER")
PASSWORD = os.getenv("SSH_PASSWORD")

def connect_SSH(HOST, USER, PASSWORD):
    client = paramiko.SSHClient()
    
    # Política para aceitar chaves de hosts desconhecidos
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Conexão forçando autenticação por senha (importante para o seu erro anterior)
        client.connect(
            hostname=HOST, 
            username=USER, 
            password=PASSWORD,
            look_for_keys=False,
            allow_agent=False
        )
        
        while True:
            # Execução do comando
            comando = input("Digite o comando: ")
            stdin, stdout, stderr = client.exec_command(comando)
            for line in stdout.readlines():
                print(line)
            erros = stderr.readlines()
            if erros:
                print(erros)

    except Exception as Error:
        print(f"Erro na conexão: {Error}")

# Executa a função
if __name__ == "__main__":
    connect_SSH(HOST, USER, PASSWORD)