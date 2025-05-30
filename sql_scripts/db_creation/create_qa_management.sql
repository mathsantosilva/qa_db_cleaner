-- Criação do banco de gerenciamento
CREATE DATABASE QA_MANAGEMENT;
GO

-- Usar o banco recém-criado
USE QA_MANAGEMENT;
GO

-- Tabela de controle dos bancos QA
CREATE TABLE bancos_qa (
    id              INT IDENTITY(1,1) PRIMARY KEY,
    nome_banco     VARCHAR(255)  NOT NULL,
    data_insercao  DATETIME      NOT NULL DEFAULT GETDATE(),
    data_expiracao DATETIME      NULL,
    pode_apagar    BIT           NOT NULL DEFAULT 0
);
GO

-- Tabela de histórico de ações em bancos QA
CREATE TABLE historico_bancos_qa (
    id              INT IDENTITY(1,1) PRIMARY KEY,
    nome_banco      VARCHAR(255) NOT NULL,
    acao            VARCHAR(50)  NOT NULL, -- exemplo: 'exclusao'
    data_acao       DATETIME     NOT NULL DEFAULT GETDATE()
);
GO
