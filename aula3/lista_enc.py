import unittest


class Noh():
    def __init__(self, valor, prox=None):
        self.prox = prox
        self.valor = valor


class Lista():
    def __init__(self):
        self.tam = 0
        self.inicio = None

    def adicionar(self, valor):
        noh = Noh(valor)
        if self.tam == 0:
            self.inicio = noh
        else:
            ultimo = self.inicio
            while ultimo.prox is not None:
                ultimo = ultimo.prox
            ultimo.prox = noh
        self.tam += 1

    def __len__(self):
        return self.tam

    def __iter__(self):
        noh_atual = self.inicio
        while noh_atual is not None:
            yield noh_atual.valor
            noh_atual = noh_atual.prox


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


class ListaTestes(unittest.TestCase):
    def test_init(self):
        lista = Lista()
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.inicio)

    def test_adicionar_em_lista_vazia(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(1, len(lista))
        inicio = lista.inicio
        self.assertEqual(0, inicio.valor)
        self.assertIsNone(inicio.prox)

    def test_adicionar_segundo_elemento(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        self.assertEqual(2, len(lista))
        inicio = lista.inicio
        self.assertEqual(0, inicio.valor)
        segundo = inicio.prox
        self.assertIsInstance(segundo, Noh)
        self.assertEqual(1, segundo.valor)
        self.assertIsNone(segundo.prox)

    def test_adicionar_terceiro_elemento(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        lista.adicionar(2)
        self.assertEqual(3, len(lista))
        inicio = lista.inicio
        self.assertEqual(0, inicio.valor)
        segundo = inicio.prox
        self.assertIsInstance(segundo, Noh)
        self.assertEqual(1, segundo.valor)
        terceiro = segundo.prox
        self.assertIsInstance(terceiro, Noh)
        self.assertEqual(2, terceiro.valor)
        self.assertIsNone(terceiro.prox)

    def test_iterar(self):
        lista = Lista()
        lista.adicionar('A')
        lista.adicionar('B')
        lista.adicionar('C')
        respostas = 'ABC'
        for resposta_esperada, resposta_real in zip(respostas, lista):
            self.assertEqual(resposta_esperada, resposta_real)
