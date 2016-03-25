import unittest


def _merge(seq_esquerda, seq_direita):
    pass


def merge_sort(seq):
    pass


class MergeTestes(unittest.TestCase):
    def test_listas_vazias(self):
        self.assertListEqual([], _merge([], []))

    def test_lista_uma_lista_unitaria(self):
        self.assertListEqual([1], _merge([1], []))

    def test_listas_unitarias(self):
        self.assertListEqual([1], _merge([1], []))

    def test_listas_unitarias(self):
        self.assertListEqual([1, 2], _merge([1], [2]))

    def test_listas_intercaladas(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6], _merge([1, 3, 5], [2, 4, 6]))


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], merge_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], merge_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], merge_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], merge_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
