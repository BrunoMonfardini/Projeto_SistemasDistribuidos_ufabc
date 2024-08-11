import socket

class Gerenciador:
    def __init__(self):
        self.servidores = [65432, 65435, 65436]  # lista com IPs ou identificadores dos servidores

    def escolher_servidores(self):
        servidor_principal = self.servidores[0]  # escolha o servidor de forma rotativa ou aleatória
        servidor_replicacao = self.servidores[1]  # escolha o servidor de réplica
        return servidor_principal, servidor_replicacao

    def envia_arquivo(self, caminho_arquivo):
        servidor_principal, servidor_replicacao = self.escolher_servidores()
        # envia o nome do arquivo e os servidores escolhidos para o cliente

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(servidor_principal)
            nome_arquivo = nome_arquivo.split('/')[-1]
            s.sendall(nome_arquivo.encode())
            with open(caminho_arquivo, 'rb') as f:
                while True:
                    dados = f.read(1024)
                    if not dados:
                        break
                    s.sendall(dados)
            print(f'Arquivo {nome_arquivo} enviado ao servidor principal {servidor_principal}')
    
if __name__ == '__main__':
    caminho_arquivo = 'path/to/your/file'  # Caminho do arquivo a ser enviado
    Gerenciador.envia_arquivo(caminho_arquivo)