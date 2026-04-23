import os
from pathlib import Path


def centralizar_janela(largura, altura, janela):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def identificar_convenio(caminho_arquivo):
    '''
    # CÉLULA 3 - IDENTIFICAR CONVÊNIO 
    '''
    nome_arquivo = os.path.basename(caminho_arquivo).upper()

    if "MEDISERVICE" in nome_arquivo:
        return "MEDISERVICE"

    if "PORTO" in nome_arquivo:
        return "PORTO SEGURO"

    if "SUL" in nome_arquivo:
        return "SULAMERICA"

    if "BRADESCO" in nome_arquivo:
        return "BRADESCO"

    if "UNIMED" in nome_arquivo:
        return "UNIMED"

    return "DESCONHECIDO"


def pegar_caminho_onde_abre_o_exe():
    caminho_arquivo = os.path.abspath(__file__)
    pasta_raiz_arquivos = os.path.dirname(caminho_arquivo)

        # Pastas de entrada
    PASTA_XML = os.path.join(pasta_raiz_arquivos, "arquivos/XML")
    PASTA_CSV = os.path.join(pasta_raiz_arquivos, "arquivos/CSV")
    PASTA_EXCEL = os.path.join(pasta_raiz_arquivos, "arquivos/EXCEL")
    pasta_logs = os.path.join(pasta_raiz_arquivos, "logs")

    # Lista de todas as pastas de entrada
    PASTAS_ENTRADA = [PASTA_XML, PASTA_CSV, PASTA_EXCEL, pasta_logs]

    # Criar pastas automaticamente se não existirem
    for pasta in PASTAS_ENTRADA:
        os.makedirs(pasta, exist_ok=True)
    
    return Path(pasta_raiz_arquivos).as_posix()
                                       

  