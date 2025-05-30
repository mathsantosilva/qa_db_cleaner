# 🧹 QA DB Cleaner

Este projeto é um utilitário Python para automatizar a **limpeza de bancos QA** em uma instância SQL Server. Ele identifica bancos marcados como "pode apagar", executa o `DROP DATABASE`, e registra a ação em uma tabela de histórico.

## 📦 Estrutura do Projeto

```
qa_db_cleaner/
├── logs/                                # Pasta para arquivos de log
│   └── qa_db_cleaner.log
│
├── src/
│   ├── __init__.py
│   ├── banco_repository.py              # Operações com controle e histórico de bancos
│   ├── config.py                        # Configurações de conexão
│   ├── database.py                      # Conexão e funções genéricas de banco
│   ├── logger.py                        # Configuração de logging para o projeto
│   └── main.py                          # Ponto de entrada
│   ├── process.py                       # Lógica de exclusão
│
├── sql_scripts/
│   └── db_creation/
│       └── create_qa_management.sql     # Script de criação do banco de controle
│   └── jobs/
│       └── job_sync_control.sql         # Script utilizado para select/insert dos bancos da instancia no banco de controle
│
├── tests/
│   ├── __init__.py
│   ├── test_banco_repository.py
│   ├── test_dropper.py
│   └── mocks/
│       └── db_mock.py
│
├── requirements.txt
└── README.md
```

## ⚙️ Funcionalidades

- 🔍 Lista todos os registros do banco `qa_management`
- ✅ Filtra os bancos com `pode_apagar = true` e `data_expiracao < GETDATE()`
- 🧨 Executa `DROP DATABASE` nesses bancos
- 📝 Registra a ação na tabela `historico_bancos_qa`
- 🗑️ Deleta o registro da tabela `bancos_qa`

## 📜 Regras
- Os bancos contidos na instancia serão adicionados no banco `bancos_qa` com expiração em 10 dias
  - Essa regra esta no script presente no job `InsertDatabases`
- Os registros contidos na tebela `bancos_qa` serão ignorados caso tenham `pode_apagar = true` mesmo que a data de expiração esteja menor que o dia atual
- Se o `drop_banco()` falhar, o programa não ira para os passos seguintes `inserir_log()` e `remover_registro()`
- Todas as ações serão logadas com o seu devido tipo `INFO`, `WARNING` e `ERROR`

## 🧩 Estrutura das Tabelas

### `bancos_qa` (Controle)

| Campo           | Tipo       | Descrição                       |
|-----------------|------------|---------------------------------|
| id              | INT        | ID autoincremento               |
| nome_banco      | VARCHAR    | Nome do banco                   |
| data_insercao   | DATETIME   | Quando foi inserido no controle |
| data_expiracao  | DATETIME   | Quando pode ser excluído        |
| pode_apagar     | BIT        | Flag para controle de limpeza   |

### `historico_bancos_qa` (Log)

| Campo           | Tipo       | Descrição                        |
|-----------------|------------|----------------------------------|
| id              | INT        | ID autoincremento                |
| nome_banco      | VARCHAR    | Nome do banco excluído           |
| acao            | VARCHAR    | Tipo de ação (ex: 'exclusao')    |
| data_acao       | DATETIME   | Data da ação executada           |

## 🚀 Como usar

1. **Configure a conexão no `.env`:**

Para manter as credenciais seguras e separar a configuração do código, este projeto utiliza um arquivo `.env`.

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```dotenv
# Configurações de conexão com o banco de dados SQL Server
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=localhost
DB_DATABASE=qa_management
DB_USERNAME=seu_usuario
DB_PASSWORD=sua_senha
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o script principal:**

```bash
python src/main.py
```

## 🧪 Testes Unitários

Use `pytest` para rodar os testes:

```bash
pytest tests/
```

## 🛡️ Boas práticas aplicadas

- Separação de responsabilidades (cada módulo faz uma coisa)
- Projeto preparado para testes unitários
- Facilmente extensível para log externo, e-mails, agendamentos etc.
- Simples de integrar com o SQL Server Agent Job

## 👨‍💻 Autor
Este projeto foi estruturado com foco em automação de ambientes de QA e manutenibilidade de longo prazo.