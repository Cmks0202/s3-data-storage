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
def read_files_exames(path_default:str) -> List[str]:
    '''Função que lê os arquivos da pasta \exames
    '''
    try:
        pasta_arquivos = os.listdir(path_default) # listagem de arquivos dentro da pasta
        arquivos: List[str] = []

        logging.info(f'Folder name: {path_default}\n Files in folder: {pasta_arquivos}')
        for arquivo in pasta_arquivos:
            arquivos.append(arquivo)
        return arquivos
    except:
        if not os.path.exists(path_default):
            logging.error(f"Diretório {path_default} não encontrado.")
        return []
    




## joga os arquivos para o s3

## pipeline (fará as outras anteriores)
