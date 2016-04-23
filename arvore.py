# class Arvore:
#     def __init__(self, valor, esquerda=None, direita=None):
#         self.direita = direita
#         self.esquerda = esquerda
#         self.valor = valor
#
#     def __iter__(self):
#         yield self.valor
#         if self.esquerda is not None:
#             for v in self.esquerda:
#                 yield v
#         if self.direita is not None:
#             for v in self.direita:
#                 yield v
#
#
#
# arvores = [Arvore(i) for i in range(10)]
# arvores[5].esquerda = arvores[2]
# arvores[5].direita = arvores[8]
#
# arvores[2].esquerda = arvores[1]
# arvores[2].direita = arvores[4]
#
# arvores[1].esquerda = arvores[0]
#
# arvores[4].esquerda = arvores[3]
#
# arvores[8].esquerda = arvores[7]
# arvores[8].direita = arvores[9]
#
# arvores[7].esquerda = arvores[6]
#
# # [5, 2, 1, 0, 4, 3, 8, 7, 6, 9]
#
# print(list(arvores[5]))

class A:
    def __init__(self, a):
        self.a = a

    def __hash__(self):
        return hash(self.a)

    def __eq__(self, other):
        if other is None or not isinstance(other, A):
            return False
        return self.a == other.a


a = A('a')
dct = {a: 'a'}
print(dct[a])
a.a='b'
print(dct[a])
