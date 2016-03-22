class Pessoa():
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return "Pessoa('%s', %s)" % (self.nome, self.idade)

    def __le__(self, other):
        return self.idade <= other.idade

    def __gt__(self, other):
        return self.idade > other.idade


pessoas = [Pessoa('renzo', 33), Pessoa('Sham', 14), Pessoa('Rafaela', 17)]


def extrair_idade(p):
    return p.nome.upper()


print(pessoas[0] <= pessoas[1])
pessoas.sort()
print(pessoas)
