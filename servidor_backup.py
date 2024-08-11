import socket
import os
import threading

# Configurações
HOST = '0.0.0.0'
PORTA = 65432
BACKUP_DIR = 'backups'

# Cria pasta de backup caso ela não existir
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def lidar_cliente(conexao, endereco, replica=False):
    print(f'Conectado por {endereco}')
    nome_arquivo = conexao.recv(1024).decode()
    caminho_arquivo = os.path.join(BACKUP_DIR, nome_arquivo)
    with open(caminho_arquivo, 'wb') as f:
        while True:
            data = conexao.recv(1024)
            if not data:
                break
            f.write(data)
    print(f'Arquivo {nome_arquivo} foi salvo.')


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
            print(f'Arquivo {nome_arquivo} replicado para {ip}:{porta}')

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORTA))
        s.listen()
        print(f'Servidor escutando em {HOST}:{PORTA}')
        while True:
            conn, addr = s.accept()
            threading.Thread(target=lidar_cliente, args=(conn, addr)).start()

if __name__ == '__main__':
    iniciar_servidor()