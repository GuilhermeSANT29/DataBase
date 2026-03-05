import sqlite3

conexao = sqlite3.connect("database.db")

print ("banco criado com sucesso")

conexao.close()