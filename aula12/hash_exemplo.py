class Pessoa:
    def __init__(self, rg, idade):
        self.idade = idade
        self.rg = rg

    def __hash__(self):
        return hash(self.rg)

    def __eq__(self, other):
        if other is None or not isinstance(other, Pessoa):
            return False
        return self.rg == other.rg and self.idade == other.idade

    def __repr__(self):
        return 'Pesso({!r},{!r})'.format(self.rg,self.idade)


renzo = Pessoa('rg', 33)
renzo_clone = Pessoa('rg', 33)
print(renzo is renzo_clone)
print(renzo == renzo_clone)
outra_pessoa = Pessoa('rg', 31)
print(renzo == outra_pessoa)
print(hash((renzo)))
dct = {renzo: 'Santos'}
renzo.idade=34
print(renzo in dct)

print(set([renzo, renzo_clone, outra_pessoa]))
