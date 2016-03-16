import time


def max(seq):
    possivel_max = float('-inf')
    for v in seq:
        if v > possivel_max:
            possivel_max = v
    return possivel_max



for i in range(1, 7):
    lista = range(10 ** i)
    inicio = time.time()
    print(max(lista))
    tempo_execucao = time.time() - inicio
    print(len(lista), tempo_execucao)

