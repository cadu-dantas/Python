import sqlite3

# conectando...
conn = sqlite3.connect('C:/ProjetosPython/EDD-DL/Gerar_Script_Sql/database/config_scripts_sql.db')
# definindo um cursor
cursor = conn.cursor()

table_name = 'config_tabelas_full'

cursor.execute("""DROP TABLE IF EXISTS """ + table_name + """;""")


# criando a tabela (schema)
cursor.execute(""" 
    CREATE TABLE """+str(table_name)+""" (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	SCHEMA	VARCHAR(50),
 	TABELA	VARCHAR(50),
    ATIVO BOOLEAN
);
""")

print('Tabela '+table_name+' criada com sucesso.')
# desconectando...
conn.close()