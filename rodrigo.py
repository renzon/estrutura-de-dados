# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest

def min_max(lista, maximo, minimo, x):
    maximo = m
    minimo = n
    if(x <= len(lista)):
        return m , n
        if (maximo < lista[x]):
            maximo = lista[x]
        if (minimo > lista[x]):
            minimo = lista[x]
        return maximo_minimo(lista, m, n, x + 1)

def min_max(lista):
    '''O programa possui uma função recursiva que retorna o maior e menor numero
da lista. O algoritimo é O(n) pois percorre a lista sem ordená-la
retornando o resultado'''
    if len(lista) == 1:
        return lista[0], lista[0]
    else:
        return min_max(lista, lista[0], lista[0], 1)

class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()