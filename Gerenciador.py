import socket
import sys

servidores = [('localhost', 65432), ('localhost', 65435), ('localhost', 65436)]  # lista com IPs ou identificadores dos servidores

def escolher_servidores():
        servidor_principal = servidores[0]  # escolha o servidor de forma rotativa ou aleatória
        servidor_replicacao = servidores[1]  # escolha o servidor de réplica
        return servidor_principal, servidor_replicacao

def envia_arquivo(servidor, servidor_replica, caminho_arquivo):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(servidor)
        nome_arquivo = caminho_arquivo.split('\\')[-1]
        s.sendall(nome_arquivo.encode('utf-8'))
        with open(caminho_arquivo, 'rb') as f:
            while True:
                dados = f.read(1024)
                if not dados:
                    break
                s.sendall(dados)
        print(f'Arquivo {nome_arquivo} enviado ao servidor principal {servidor}')
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(servidor_replica)
        nome_arquivo = caminho_arquivo.split('\\')[-1]
        s.sendall(nome_arquivo.encode('utf-8'))
        with open(caminho_arquivo, 'rb') as f:
            while True:
                dados = f.read(1024)
                if not dados:
                    break
                s.sendall(dados)
        print(f'Arquivo réplica {nome_arquivo} enviado ao servidor {servidor_replica}')

if __name__ == '__main__':
    caminho_arquivo = sys.argv[1:][0]
    servidores_escolhidos = escolher_servidores()
    envia_arquivo(servidores_escolhidos[0], servidores_escolhidos[1], caminho_arquivo)