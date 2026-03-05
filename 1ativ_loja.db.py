import sqlite3

conexao = sqlite3.connect("loja.db")

print ("banco criado com sucesso")

conexao.close()