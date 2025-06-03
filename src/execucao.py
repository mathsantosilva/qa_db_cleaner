from src.config import *
from datetime import *

formato = "%d-%m-%Y-%H-%M"

def validar_execucao():
    config = carregar_ou_criar_config()
    data = datetime.now()
    data_str = data.strftime(formato)
    if config['ultima_execucao']:
        ultima_execucao = datetime.strptime(config['ultima_execucao'], formato)
        tempo_de_espera = config['tempo_de_espera']
        if (data - ultima_execucao).days > tempo_de_espera:
            load_dados_execucao(config, data_str)
            return True
        else:
            return False

    else:
        load_dados_execucao(config, data_str)
        return True

def load_dados_execucao(config, data_str):
    config['ultima_execucao'] = data_str
    carregar_ou_criar_config(config)