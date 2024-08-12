import socket
import os
import threading

from constants import BACKUP_DIR, HOST

class Servidor:
    def __init__(self, porta):
        self.porta = porta
        self.dir = BACKUP_DIR + f"{porta}"
    
    def lidar_diretorio_backup(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def lidar_cliente(self, conexao, endereco):
        print(f'Conectado por {endereco}')
        nome_arquivo = conexao.recv(1024).decode('utf-8')
        caminho_arquivo = os.path.join(self.dir, nome_arquivo)
        with open(caminho_arquivo, 'wb') as f:
            while True:
                data = conexao.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f'Arquivo {nome_arquivo} foi salvo.')
    
    def replicar_arquivo(servidor_replica, caminho_arquivo):
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
    
    def iniciar_servidor(self):
        self.lidar_diretorio_backup()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, self.porta))
            s.listen()
            print(f'Servidor escutando em {HOST}:{self.porta}')
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.lidar_cliente, args=(conn, addr)).start()

if __name__ == '__main__':
    servidores = [Servidor(porta=65432), Servidor(porta=65435), Servidor(porta=65436)]
    for servidor in servidores:
        threading.Thread(target=servidor.iniciar_servidor).start()
