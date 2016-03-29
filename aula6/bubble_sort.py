import unittest


def bubble_sort(seq):
    n=len(seq)-1
    for i_corrente in range(n):
        for i in range(n):
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
                flag=True
        if (flag==False):
             break
        flag=False
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([7, 9, 1, 0, 5, 3, 6, 2, 4, 8]))
    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    unittest.main()
