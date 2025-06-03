from dotenv import load_dotenv
import yaml
from src.logger import *

config = None

CONFIG_PATH = "config.yaml"

# Valores padrão
config_padrao = {
    "ultima_execucao": None,
    "tempo_de_espera": 10  # em dias
}

def carregar_ou_criar_config(config_atual=None):
    if not os.path.exists(CONFIG_PATH):
        logger.warning("Arquivo de configuração não encontrado. Criando com padrão...")
        with open(CONFIG_PATH, "w") as f:
            yaml.dump(config_padrao, f)
        return config_padrao
    else:
        try:
            with open(CONFIG_PATH, "r") as f:
                config = yaml.safe_load(f) or {}

            if config_atual:
                with open(CONFIG_PATH, "w") as f:
                    yaml.dump(config_atual, f)
                config = config_atual
        except Exception as e:
            with open(CONFIG_PATH, "w") as f:
                yaml.dump(config_padrao, f)
                with open(CONFIG_PATH, "r") as f:
                    config = yaml.safe_load(f) or {}

                if config_atual:
                    with open(CONFIG_PATH, "w") as f:
                        yaml.dump(config_atual, f)
                    config = config_atual
        return config

# Carrega as variáveis do .env
if not load_dotenv():
    logger.error("Arquivo de configuração .env não encontrado")

DB_CONFIG = {
    "driver": os.getenv("DB_DRIVER"),
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_DATABASE"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
}