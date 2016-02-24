import unittest


class Noh():
    pass


class Lista():
    pass


class NohTestes(unittest.TestCase):
    def test_init_com_valores_padrao(self):
        noh = Noh(4)
        self.assertEqual(4, noh.valor)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)

    def test_init_com_no_esquerdo(self):
        esquerdo = Noh(1)
        noh = Noh(2, esquerdo)
        self.assertEqual(esquerdo, noh.esquerdo)
        self.assertIsNone(noh.direito)
        noh3 = Noh(3, esquerdo=esquerdo)
        self.assertEqual(esquerdo, noh3.esquerdo)
        self.assertIsNone(noh3.direito)

    def test_init_com_no_direito(self):
        direito = Noh(1)
        noh = Noh(2, direito=direito)
        self.assertEqual(direito, noh.direito)
        self.assertIsNone(noh.esquerdo)

    def test_init_com_no_esquerdo_e_direito(self):
        esquerdo = Noh(1)
        direito = Noh(2)
        noh = Noh(3, esquerdo, direito)
        self.assertEqual(esquerdo, noh.esquerdo)
        self.assertEqual(direito, noh.direito)


class ListaTestes(unittest.TestCase):
    def test_init(self):
        lista = Lista()
        self.assertEquals(0, lista.tam)
        self.assertIsNone(lista.primeiro)
        self.assertIsNone(lista.ultimo)

    def test_adicionar(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        self.assertEqual(primeiro, lista.ultimo)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(primeiro.direito)

        lista.adicionar(1)
        self.assertEqual(2, lista.tam)
        primeiro_2 = lista.primeiro
        self.assertEqual(primeiro, primeiro_2)
        ultimo = lista.ultimo
        self.assertEqual(1, ultimo.valor)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(ultimo, primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

        segundo = ultimo
        lista.adicionar(2)
        self.assertEqual(3, lista.tam)
        primeiro_3 = lista.primeiro
        self.assertEqual(primeiro, primeiro_3)
        ultimo = lista.ultimo
        self.assertNotEqual(segundo, ultimo)
        self.assertEqual(2, ultimo.valor)

        self.assertEqual(primeiro, segundo.esquerdo)
        self.assertEqual(segundo, primeiro.direito)

        self.assertEqual(segundo, ultimo.esquerdo)
        self.assertEqual(ultimo, segundo.direito)

        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_adicionar_primeiro(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        self.assertEqual(primeiro, lista.ultimo)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(primeiro.direito)

    def test_adicionar_segundo(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        self.assertEqual(2, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        ultimo = lista.ultimo
        self.assertEqual(1, ultimo.valor)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(ultimo, primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_adicionar_terceiro(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        lista.adicionar(3)
        self.assertEqual(3, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        ultimo = lista.ultimo
        segundo = primeiro.direito
        self.assertEqual(1, segundo.valor)
        self.assertEqual(2, ultimo.valor)

        self.assertEqual(primeiro, segundo.esquerdo)

        self.assertEqual(segundo, ultimo.esquerdo)
        self.assertEqual(ultimo, segundo.direito)

        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)


if __name__ == '__main__':
    unittest.main()
