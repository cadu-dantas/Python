import sqlite3

# conectando...
conn = sqlite3.connect('C:/ProjetosPython/EDD-DL/Gerar_Script_Sql/database/config_scripts_sql.db')
# definindo um cursor
cursor = conn.cursor()

table_name = 'config_scripts'

#cursor.execute("""DROP TABLE """ + table_name + """;""")


# criando a tabela (schema)
cursor.execute(""" 
    CREATE TABLE """+str(table_name)+""" (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ID_DATABASE VARCHAR(50),
	IP VARCHAR(15),
	ATIVO BOOLEAN,
	DATABASE_NAME VARCHAR(255)
);
""")

print('Tabela '+table_name+' criada com sucesso.')
# desconectando...
conn.close()