import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""
                DELETE FROM CLIENTES
                WHERE ID = 2
                """)

conexao.commit()
conexao.close()

print("Registro removido com sucesso!")