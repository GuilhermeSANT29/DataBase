import unittest

def media (a, b):
    return (a + b) / 2

class testeMedia (unittest.TestCase):

    def test_media_notas (self):
        self.assertEqual (media(8,10), 9)

    def teste_media_zero (self):
        self.assertEqual(media(0,0), 0)

if __name__ == "__main__":
    unittest.main()