import sqlite3

conn = sqlite3.connect('C:/ProjetosPython/EDD-DL/Gerar_Script_Sql/database/config_scripts_sql.db')
cursor = conn.cursor()

cursor.execute("""DELETE FROM config_tabelas;""")

cursor.execute("""
INSERT INTO config_tabelas (SCHEMA, TABELA, COLUNA_CRIACAO, COLUNA_ATUALIZACAO, ATIVO, TIPO)
VALUES 
('public','cad_produtos_ean_alternativo','','','false','HML'),
('public','categorias_ims','','','false','HML'),
('public','clientes_nao_cadastrados','','','false','HML'),
('public','configuracao_demanda','','','false','HML'),
('public','conferencia_conformidade','','','false','HML'),
('public','controle_vigencias','created_at','updated_at','false','HML');
""")
#pode add todas as tabelas da sua base 
# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()