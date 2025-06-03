import logging
from logging.handlers import RotatingFileHandler
import os

# Garante que a pasta logs exista
os.makedirs(f"./logs", exist_ok=True)

log_file = "./logs/qa_db_cleaner.log"

logger = logging.getLogger("qa_cleaner")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Força o flush a cada log emitido
file_handler.flush = lambda: file_handler.stream.flush()

# Wrap do emit pra sempre flushar
original_emit = file_handler.emit


def emit_and_flush(record):
    original_emit(record)
    file_handler.flush()


file_handler.emit = emit_and_flush

logger.addHandler(file_handler)