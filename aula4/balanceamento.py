import unittest

## Código para adicionar path do projeto
import sys
from os import path

file_path = path.abspath(__file__)
projeto_path = path.join(file_path, '..', '..')
projeto_path = path.abspath(projeto_path)
sys.path.append(projeto_path)


## Fim

def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados

    O Aluno deverá informar a complexidade de tempo e espaço da função

    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior

    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    pass


class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
