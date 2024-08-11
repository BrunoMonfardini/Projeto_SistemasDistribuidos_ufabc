import socket
import os
import threading

# Configurações
HOST = '0.0.0.0'
PORT = 65432
BACKUP_DIR = 'backups'

# Cria pasta de backup caso ela não existir
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

class Servidor:
    def __init__(self, id):
        self.id = id
        self.diretorio_raiz = f"/servidores/servidor_{id}/"

    def receber_arquivo(self, nome_arquivo, dados):
        caminho = os.path.join(self.diretorio_raiz, nome_arquivo)
        with open(caminho, 'wb') as f:
            f.write(dados)

    def replicar_arquivo(nome_arquivo, ip, porta):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, porta))
                s.sendall(nome_arquivo.encode())
                filepath = os.path.join(BACKUP_DIR, nome_arquivo)
                with open(filepath, 'rb') as f:
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        s.sendall(data)
                print(f'File {nome_arquivo} replicated to {ip}:{porta}')
