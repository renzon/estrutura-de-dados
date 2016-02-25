import unittest


class Noh():
    def __init__(self, valor, prox=None):
        self.prox = prox
        self.valor = valor


class Lista():
    def __init__(self):
        self.tam = 0
        self.inicio = None


class NohTestes(unittest.TestCase):
    def test_init(self):
        noh = Noh(1)
        self.assertEqual(1, noh.valor)
        self.assertIsNone(noh.prox)

    def test_init_prox(self):
        prox = Noh(2)
        noh = Noh(1, prox)
        self.assertEqual(1, noh.valor)
        self.assertEqual(prox, noh.prox)

    pass


class ListaTestes(unittest.TestCase):
    def test_init(self):
        lista = Lista()
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.inicio)
