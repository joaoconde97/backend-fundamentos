import json
import os

def carregar_lancamentos():
    caminho_arquivo = "doc_lancamentos.txt"

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            lancamentos = json.load(arquivo)
            return lancamentos
    
    else:
        return []
    
def salvar_lancamentos(lancamentos):
    caminho_arquivo = "doc_lancamentos.txt"

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lancamentos, arquivo)
