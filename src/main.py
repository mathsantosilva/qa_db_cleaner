from src.process import *
from src.logger import logger

if __name__ == "__main__":
    logger.info(f"Rotina iniciada.")
    bancos = exe_list_databases()
    if bancos:
        for nome_banco in bancos:
            result_drop = process_drop_database(nome_banco)
            if process_insert_log(result_drop, nome_banco):
                process_delete_register(nome_banco)
    logger.info("Rotina finalizada")