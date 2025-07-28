import os
import shutil

# Organiza arquivos da pasta atual em subpastas por extensão
def organizar_por_extensao(diretorio="."):
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho):
            _, extensao = os.path.splitext(arquivo)
            if extensao:
                pasta_destino = os.path.join(diretorio, extensao[1:].lower())
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho, os.path.join(pasta_destino, arquivo))
                print(f"Movido: {arquivo} -> {pasta_destino}/")

# Executa no diretório atual
organizar_por_extensao()
