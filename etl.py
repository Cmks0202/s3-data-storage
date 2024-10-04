## imports
import os
import boto3
import pandas as pd
import logging
from typing import List
# from doenv import load_dotenv




# settings general
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Para enviar a saída para o console
    ]
)


## functions read files 
def read_files_exames() -> List[str]:
    '''Função que lê os arquivos da pasta \exames
    '''
    try:
        path_default = r'C:\Users\milas\Downloads\exames' # caminho da pasta
        pasta_arquivos = os.listdir(path_default) # listagem de arquivos dentro da pasta
        arquivos: List[str] = []

        logging.info(f'Arquivos dentro da pasta:\n{pasta_arquivos}')
        for arquivo in pasta_arquivos:
            arquivos.append(arquivo)
        return arquivos
    except:
        if not os.path.exists(path_default):
            logging.error(f"Diretório {path_default} não encontrado.")
        return []
    

oi = read_files_exames()
print


## joga os arquivos para o s3

## pipeline (fará as outras anteriores)
