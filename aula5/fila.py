import unittest
from collections import deque


class Fila():
    def __init__(self):
        self._deque = deque()

    def enfileirar(self, valor):
        return self._deque.append(valor)

    def vazia(self):
        return len(self._deque) == 0

    def primeiro(self):
        try:
            return self._deque[0]
        except IndexError:
            raise FilaVaziaErro

    def desenfileirar(self):
        try:
            return self._deque.popleft()
        except IndexError:
            raise FilaVaziaErro


class FilaVaziaErro(Exception):
    pass


class FilaTestes(unittest.TestCase):
    def test_primeiro_fila_vazia(self):
        fila = Fila()
        self.assertTrue(fila.vazia())
        self.assertRaises(FilaVaziaErro, fila.primeiro)

    def test_enfileirar_um_elemento(self):
        fila = Fila()
        fila.enfileirar('A')
        self.assertFalse(fila.vazia())
        self.assertEqual('A', fila.primeiro())

    def test_enfileirar_dois_elementos(self):
        fila = Fila()
        fila.enfileirar('A')
        fila.enfileirar('B')
        self.assertFalse(fila.vazia())
        self.assertEqual('A', fila.primeiro())

    def test_desenfileirar_fila_vazia(self):
        fila = Fila()
        self.assertRaises(FilaVaziaErro, fila.desenfileirar)

    def test_desenfileirar(self):
        fila = Fila()
        letras = 'ABCDE'
        for letra in letras:
            fila.enfileirar(letra)

        for letra in letras:
            letra_desemfileirada = fila.desenfileirar()
            self.assertEqual(letra, letra_desemfileirada)
