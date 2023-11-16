import sqlite3

#caminho da pasta do projeto 
conn = sqlite3.connect('C:/ProjetosPython/EDD-DL/Gerar_Script_Sql/database/config_scripts_sql.db')
cursor = conn.cursor()


cursor.execute("""DELETE FROM config_scripts_sql;""")

cursor.execute("""
INSERT INTO config_scripts (ID_DATABASE, IP, ATIVO, DATABASE_NAME)
VALUES ('CLIENTE_1','33.222.111.33','TRUE','base_name'),
('CLIENTE_2','33.222.111.11','TRUE','base_name'),
(;
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()