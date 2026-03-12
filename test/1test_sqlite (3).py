import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""
               INSERT INTO CLIENTES (NOME, IDADE)
               VALUES ("GUI", 20), ("TUCO", 21), ("CAWA", 22), ("MIGUEL", 23), ("GUSTAVO", 24), ("LUCAS", 25), ("PEDRO", 26), ("JOAO", 27), ("MARIA", 28), ("ANA", 29)
               """)

conexao.commit()
conexao.close()

print("DADOS INSERIDOS COM SUCESSO")