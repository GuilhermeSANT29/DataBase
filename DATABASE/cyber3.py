import unittest

def login(usuario):
    sql = f"SELECT * FROM usuarios WHERE login='{usuario}'"
    return sql

class TesteSeguranca(unittest.TestCase):

    def test_sql_injection(self):
        ataque = "' OR 1=1 --"
        resultado = login(ataque)

        self.assertIn("OR 1=1", resultado)

if __name__ == '__main__':
    unittest.main()