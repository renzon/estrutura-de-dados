class MeuErro(Exception):
    pass


lista = None
try:
    erro=MeuErro('Meu erro')
    raise erro
    # lista.append(1)
    # print(lista[1])
    print('Tentativa')
except IndexError:
    print('Erro de índice')
except AttributeError:
    print('Erro de None')
else:
    print('Else')
