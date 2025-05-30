from src.process import *
from src.logger import logger

if __name__ == "__main__":
    logger.info(f"Rotina iniciada.")
    processar_bancos()
    logger.info("Rotina finalizada")