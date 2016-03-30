import unittest


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq.pop()
    menores = [e for e in seq if e < pivot]
    maiores_ou_iguais = [e for e in seq if e >= pivot]
    menores_ordenados=quick_sort(menores)
    maiores_ordenados=quick_sort(maiores_ou_iguais)
    menores_ordenados.append(pivot)
    return menores_ordenados+maiores_ordenados



class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
