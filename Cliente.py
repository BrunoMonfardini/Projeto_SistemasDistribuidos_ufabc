import os
import sys

def listar_arquivos(diretorio):
    return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]

diretorio_raiz = "cliente"

def main():
    print("Escolha um arquivo para enviar:")
    files = listar_arquivos(diretorio_raiz)
    for idx, file in enumerate(files):
        print(f"{idx + 1}: {file}")

    escolha = int(input("Digite o número do arquivo: ")) - 1

    if 0 <= escolha < len(files):
        caminho_arquivo = os.path.join(diretorio_raiz, files[escolha])
        print(caminho_arquivo)
        print(f"Enviando arquivo {caminho_arquivo}...")
        os.system(f'python gerenciador.py {caminho_arquivo}')
    else:
        print("Escolha inválida.")
    
if __name__ == '__main__':
    main()

