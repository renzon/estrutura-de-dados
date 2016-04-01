import unittest


def escolher_pivot_e_posicionar_no_fim(seq, inicio, fim):
    if inicio < fim:
        meio = (fim + inicio) // 2
        candidatos = [(seq[inicio], inicio), (seq[meio], meio), (seq[fim], fim)]
        candidatos.sort()
        pivot, indice_pivot = candidatos[1]
        trocar(seq, indice_pivot, fim)
        return pivot


def trocar(seq, i, i2):
    seq[i], seq[i2] = seq[i2], seq[i]


def quick_sort(seq):
    if not seq:
        return seq
    pilha = [(0, len(seq) - 1)]
    while pilha:
        inicio, fim = pilha.pop()
        pivot = escolher_pivot_e_posicionar_no_fim(seq, inicio, fim)
        esquerda = inicio
        direita = fim - 1

        while esquerda <= direita:
            while esquerda <= direita and seq[esquerda] < pivot:
                esquerda += 1
            while esquerda <= direita and seq[direita] > pivot:
                direita -= 1
            if esquerda <= direita:
                trocar(seq, esquerda, direita)
                esquerda += 1
                direita -= 1
        trocar(seq, esquerda, fim)
        if esquerda - 1 > inicio:
            pilha.append((inicio, esquerda - 1))
        if esquerda + 1 < fim:
            pilha.append((esquerda + 1, fim))
    return seq


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
