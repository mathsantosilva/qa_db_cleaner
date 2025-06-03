from src.logger import logger
import pyodbc
from src.config import DB_CONFIG

def get_connection(query, acao=None):
    result = False
    if DB_CONFIG['driver']:
        conn_str = (
            f"DRIVER={{{DB_CONFIG['driver']}}};"
            f"SERVER={DB_CONFIG['server']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"UID={DB_CONFIG['username']};"
            f"PWD={DB_CONFIG['password']};"
        )
        try:
            with pyodbc.connect(conn_str, autocommit=True) as conn:
                cursor = conn.cursor()
                if 'SELECT' in query:
                    cursor.execute(query)
                    response = cursor.fetchall()
                    if response:
                        result = [row.nome_banco for row in response]
                else:
                    if acao:
                        cursor.execute(query,acao)
                    else:
                        cursor.execute(query)
                    result = True
        except Exception as e:
            erro = str(e)
            logger.error(f"Não foi possivel realizar comando SQL devido ao seguinte erro: {erro}")
            return erro
    else:
        return False
    return result
