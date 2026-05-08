import unittest

def login(usuario, senha):
    return usuario == "admin" and senha == "123"

def acessar_painel():
    return "Painel aberto"

class TesteSistema(unittest.TestCase):

    def test_fluxo_completo(self):
        acesso = login("admin", "123")
        self.assertTrue(acesso)

        painel = acessar_painel()
        self.assertEqual(painel, "Painel aberto")

if __name__ == '__main__':
    unittest.main()