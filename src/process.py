from src.database import get_connection
from src.banco_repository import *
from src.logger import logger

def processar_bancos():
    bancos = listar_bancos_para_excluir()
    if bancos:
        for banco in bancos:
            if drop_banco(banco):
                if inserir_log(banco):
                    remover_registro(banco)

def drop_banco(banco):
    try:
        result = excluir_bancos(banco)
        return result
    except Exception as e:
        logger.error(f"Erro ao excluir banco {banco}: {e}")
        return False

def inserir_log(banco):
    try:
        registrar_historico(banco, "exclusao")
        logger.info(f"Registro inserido na tabela de log. - {banco}")
        return True
    except Exception as e:
        logger.error(f"Erro ao inserir registro na tabela de log para {banco}: {e}")
        return False

def remover_registro(banco):
    try:
        excluir_registro(banco)
        logger.info(f"Registro excluído da tabela controle. - {banco}")
    except Exception as e:
        logger.error(f"Erro ao excluir registro da tabela controle para {banco}: {e}")