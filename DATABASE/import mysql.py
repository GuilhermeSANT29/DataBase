import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="escola"
)

cursor = conexao.cursor()

sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
dados = ("Aluno", 30, "Python")

cursor.execute(sql, dados)
conexao.commit()

print("Aluno cadastrado com sucesso!")

cursor.close()
conexao.close()

