import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM PRODUTOS")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conexao.close()