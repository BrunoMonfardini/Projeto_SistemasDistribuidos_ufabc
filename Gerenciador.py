class Gerenciador:
    def __init__(self):
        self.servidores = []  # lista com IPs ou identificadores dos servidores

    def escolher_servidores(self):
        servidor_principal = self.servidores[0]  # escolha o servidor de forma rotativa ou aleatória
        servidor_replicacao = self.servidores[1]  # escolha o servidor de réplica
        return servidor_principal, servidor_replicacao

    def receber_requisicao_backup(self, nome_arquivo):
        servidor_principal, servidor_replicacao = self.escolher_servidores()
        # envia o nome do arquivo e os servidores escolhidos para o cliente
