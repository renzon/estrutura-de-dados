def gerar_lista_infinita(inicio):
    print('Inicio')
    while True:
        yield inicio
        inicio += 1


for i in gerar_lista_infinita(1):
    print(i)
