def seg_maior_que_zero(funcao):
    def nova_funcao(j):
        if j>0:
            return funcao(j)
        raise ValueError('Valor deveria ser positivo')
    return nova_funcao

@seg_maior_que_zero
def g(i):
    print('Executando %s'%i)

# g=seg_maior_que_zero(g)

g(2)
g(0)
