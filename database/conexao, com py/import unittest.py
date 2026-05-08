import unittest

usuarios = []

def cadastrar(nome):
    usuarios.append(nome)

def listar():
    return usuarios

class TesteIntegracao(unittest.TestCase):

    def test_cadastro_listagem(self):
        cadastrar("william")
        self.assertin("william", listar ())

if __name__ == "__main__":
    unittest.main()