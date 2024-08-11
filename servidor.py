import os

class Servidor:
    def __init__(self, id):
        self.id = id
        self.diretorio_raiz = f"/servidores/servidor_{id}/"

    def receber_arquivo(self, nome_arquivo, dados):
        caminho = os.path.join(self.diretorio_raiz, nome_arquivo)
        with open(caminho, 'wb') as f:
            f.write(dados)

    def enviar_replicacao(self, servidor_replicacao, nome_arquivo, dados):
        # Envia o arquivo para o servidor de réplica