import unittest

usuarios = []

def cadastrar(nome):
    usuarios.append(nome)

def listar():
    return usuarios

class TesteIntegracao(unittest.TestCase):

    def test_cadastro_listagem(self):
        cadastrar("William")
        self.assertIn("William", listar())

if __name__ == '__main__':
    unittest.main()