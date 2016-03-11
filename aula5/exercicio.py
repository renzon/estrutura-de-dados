from aula5.fila import Fila


class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao):
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    Transforma inteiros em ints
    Flutuantes em floats
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    pass


def analise_sintatica(fila):
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn pilha para avaliacao

    :param fila: fila proveniente de análise lexica
    :return: pilha com elementos tokens de numeros
    """
    pass


import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual(1, fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual(2.0, fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        fila = analise_lexica('1/{2.0+3*[7-(5-3)]}')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('3', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('7', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('5', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('3', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        pilha = analise_sintatica(fila)
        self.assertEqual(1234567890, pilha.desempilhar())
        self.assertTrue(pilha.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        pilha = analise_sintatica(fila)
        self.assertEqual(1234567890.4, pilha.desempilhar())
        self.assertTrue(pilha.vazia())

    def test_erro_float_com_2_pontos(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila.enfileirar('.')
        fila.enfileirar('5')
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_erro_2_sinais(self):
        fila = analise_sintatica('1+-2')
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1/{2.0+3*[7-(5-3)]}')
        pilha = analise_sintatica(fila)
        self.assertEqual('}', pilha.pop())
        self.assertEqual(']', pilha.pop())
        self.assertEqual(')', pilha.pop())
        self.assertEqual(3, pilha.pop())
        self.assertEqual('-', pilha.pop())
        self.assertEqual(5, pilha.pop())
        self.assertEqual('-', pilha.pop())
        self.assertEqual(7, pilha.pop())
        self.assertEqual('[', pilha.pop())
        self.assertEqual('*', pilha.pop())
        self.assertEqual(3, pilha.pop())
        self.assertEqual('+', pilha.pop())
        self.assertEqual(2.0, pilha.pop())
        self.assertEqual('{', pilha.pop())
        self.assertEqual('/', pilha.pop())
        self.assertEqual(1, pilha.pop())


if __name__ == '__main__':
    unittest.main()
