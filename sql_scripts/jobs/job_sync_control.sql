INSERT INTO qa_management.[dbo].[bancos_qa] (nome_banco, data_insercao, data_expiracao, pode_apagar)
SELECT db.name, GETDATE(), DATEADD(DAY, 10, GETDATE()), 1
FROM sys.databases db
LEFT JOIN qa_management.[dbo].[bancos_qa] cb ON cb.nome_banco = db.name
WHERE cb.nome_banco IS NULL
  AND db.database_id > 4;  -- evita bancos de sistema