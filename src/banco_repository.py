from src.database import get_connection
from src.logger import logger

def listar_bancos_para_excluir():
    query = '''
    SELECT [nome_banco] FROM qa_management.[dbo].[bancos_qa] 
    WHERE pode_apagar = 1
      AND data_expiracao <= GETDATE();
    '''
    result = get_connection(query)
    if result:
        logger.info(f"Consulta dos bancos realiza com sucesso. - {len(result)}")
    else:
        logger.warning(f"Consulta dos bancos não retornou resultados.")

    return result

def excluir_bancos(nome_banco):
    query = f'''
    DROP DATABASE [{nome_banco}]
    '''
    result = get_connection(query)
    if result:
        logger.info(f"Drop Database realizado com sucesso. - {nome_banco}")
    elif result is None:
        logger.warning(f"Banco será retirado da lista por não existir. - {nome_banco}")
        return True
    else:
        logger.error(f"Erro ao realizar Drop Database {nome_banco} - {result}.")

    return result


def registrar_historico(nome_banco, acao):
    query = '''
    INSERT INTO historico_bancos_qa (nome_banco, acao, data_acao)
    VALUES (?, ?, GETDATE())
    '''
    result = get_connection(query, (nome_banco, acao))
    if result:
        logger.info(f"Inserido o Log de Drop Database. {nome_banco}")
    else:
        logger.warning(f"Erro ao inserir registro do Drop Database no banco de log. {nome_banco}")

    return result


def excluir_registro(nome_banco):
    query = '''
    DELETE FROM [dbo].[bancos_qa]
    where [nome_banco] = (?)
    '''
    result = get_connection( query, (nome_banco))
    if result:
        logger.info(f"Excluido com sucesso registro do banco de controle. {nome_banco}")
    else:
        logger.warning(f"Erro ao Realizar exclusão do registro no banco de controle. {nome_banco}")

    return result

