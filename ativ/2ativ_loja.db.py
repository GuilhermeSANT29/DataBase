import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS produtos(
               id_produtos INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               categoria TEXT,
               preco REAL,
               quantidade INTEGER
)
""")

print("TABELA 1 CRIADOS")

conexao.commit()
conexao.close()



import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS vendas (
               id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
               produto TEXT,
               quantidade INTEGER,
               valor_total REAL,
               data_venda TEXT
)
""")

print("TABELA 2 CRIADOS")

conexao.commit()
conexao.close()