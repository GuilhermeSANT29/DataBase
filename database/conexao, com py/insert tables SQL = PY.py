import unittest
import mysql.connector

class TestIntegracaoBanco(unittest.TestCase):
    def test_inserir_aluno(self):
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

        cursor.execute("SELECT nome FROM alunos WHERE nome='Ana' ")
        resultado = cursor.fetchone()

        self.assertEqual(resultado[0], "Ana")

        cursor.close()
        conexao.close()

if __name__ == '__main__':
    unittest.main()