import os

class Cliente:
    def __init__(self):
        self.diretorio_raiz = "/cliente/"

    def selecionar_arquivo(self):
        nome_arquivo = input("Digite o nome do arquivo: ")
        caminho_arquivo = os.path.join(self.diretorio_raiz, nome_arquivo)
        with open(caminho_arquivo, 'rb') as f:
            dados = f.read()
        return nome_arquivo, dados

    def enviar_arquivo(self, nome_arquivo, dados):
        # Envia o arquivo para o gerenciador
