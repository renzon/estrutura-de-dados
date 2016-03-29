import unittest


def selection_sort(seq):
    n = len(seq)
    for i_corrente in range(n):
        _, i_min = min((seq[i], i) for i in range(i_corrente, n))
        seq[i_corrente], seq[i_min] = seq[i_min], seq[i_corrente]  # swap
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], selection_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], selection_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], selection_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], selection_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
