from src.process import *
from src.logger import *
from src.execucao import *
import time

prog_loop = True
pausa_1_dia = 60 * 60 * 24

if __name__ == "__main__":
    logger.info("Rotina iniciada")
    while prog_loop:
        try:
            if validar_execucao():
                logger.info("Iniciando execução")
                bancos = exe_list_databases()
                if bancos:
                    for nome_banco in bancos:
                        result_drop = process_drop_database(nome_banco)
                        if process_insert_log(result_drop, nome_banco):
                            process_delete_register(nome_banco)
                logger.info("Execução Finalizada")

            else:
                time.sleep(pausa_1_dia)
                continue
        except Exception as e:
            prog_loop = False
            break
    logger.info("Rotina finalizada")
