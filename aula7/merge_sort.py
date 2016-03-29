import unittest


def _merge(seq_esquerda, seq_direita):
    n_esquerda = len(seq_esquerda)
    n_direita = len(seq_direita)
    lista_mesclada = [0] * (n_direita + n_esquerda)
    i_esquerda = i_direita = 0
    while i_direita + i_esquerda < len(lista_mesclada):
        if i_esquerda < n_esquerda and (i_direita == n_direita or seq_esquerda[i_esquerda] < seq_direita[i_direita]):
            lista_mesclada[i_esquerda + i_direita] = seq_esquerda[i_esquerda]
            i_esquerda += 1
        else:
            lista_mesclada[i_esquerda + i_direita] = seq_direita[i_direita]
            i_direita += 1

    return lista_mesclada


def merge_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    metade = n // 2
    esquerda = merge_sort(seq[:metade])
    direita = merge_sort(seq[metade:])
    return _merge(esquerda, direita)


class MergeTestes(unittest.TestCase):
    def test_listas_vazias(self):
        self.assertListEqual([], _merge([], []))

    def test_lista_uma_lista_unitaria(self):
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

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], merge_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
