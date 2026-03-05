import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS CLIENTES (
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NOME TEXT,
               IDADE INTEGER
)
               """)

print("TABELA CRIADOS")

conexao.commit()
conexao.close()

print