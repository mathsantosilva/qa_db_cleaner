from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

DB_CONFIG = {
    "driver": os.getenv("DB_DRIVER"),
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_DATABASE"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
}