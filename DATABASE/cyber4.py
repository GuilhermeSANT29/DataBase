import sqlite3

usuario = input("Digite o login: ")

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

sql = "SELECT * FROM usuarios WHERE login=?"

cursor.execute(sql, (usuario,))

resultado = cursor.fetchall()

print(resultado)

conexao.close()