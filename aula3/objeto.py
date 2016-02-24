class Pessoa():
    def __init__(self, nome=None, idade=0):
        self.idade = idade
        self.nome = nome

    def cumprimetar(self):
        return 'Olá, meu nome é %s' % self.nome


renzo = Pessoa('Renzo', 33)

raphael = Pessoa('Raphael')


def imprimir(pessoa):
    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.cumprimetar())


imprimir(renzo)
imprimir(raphael)
