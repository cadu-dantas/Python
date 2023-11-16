import sqlite3

conn = sqlite3.connect('C:/ProjetosPython/EDD-DL/Gerar_Script_Sql/database/config_scripts_sql.db')
cursor = conn.cursor()

cursor.execute("""DELETE FROM config_tabelas_full;""")

cursor.execute("""
INSERT INTO config_tabelas_full (SCHEMA, TABELA, ATIVO)
VALUES 
('public','pbm_devolucoes','false'),
('public','pbm_reposicao_direta','false'),
('public','pbm_vendas','false'),
-- SEGUNDA PARTE  
('public','cad_produtos_ean_alternativo','true'),
('public','lotes_ressarcimento_financeiro','true');
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()