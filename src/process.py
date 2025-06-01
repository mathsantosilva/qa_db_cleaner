from src.database import get_connection
from src.banco_repository import *
from src.logger import logger

def process_drop_database(nome_banco):
    acao = 'exclusao'
    try:
        result = exe_drop_database(nome_banco)
    except Exception as e:
        logger.error(f"Erro ao excluir banco {nome_banco}: {e}")
    return result

def process_insert_log(result_drop, nome_banco):
    acao = "exclusao"
    try:
        if "3701" in result_drop or "não existe" in result_drop.lower():
            obs = 'Banco inexistente, registro excluído da tabela de controle'
        else:
            obs = 'Exclusão periódica'
    except:
        obs = 'Exclusão periódica'
    try:
        result = exe_insert_log(nome_banco, acao, obs)
    except Exception as e:
        logger.error(f"Erro ao inserir registro na tabela de log para {nome_banco}: {e}")
        return False
    return result

def process_delete_register(nome_banco):
    try:
        result = exe_delete_register(nome_banco)
    except Exception as e:
        logger.error(f"Erro ao excluir registro da tabela controle para {nome_banco}: {e}")
    return result