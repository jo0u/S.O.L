import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('registro_ocorrencia.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO topicos (tipo) VALUES ('Salvamento Não Fatal')")
cursor.execute("INSERT INTO topicos (tipo) VALUES ('Criança Encontrada')")
cursor.execute("INSERT INTO topicos (tipo) VALUES ('S.O.S')")

conn.commit()
conn.close()