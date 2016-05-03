import time

cont = 0

cache = [0, 1]


def fib(n):
    global cont
    cont += 1
    if n < len(cache):
        return cache[n]
    resultado = fib(n - 1) + fib(n - 2)
    cache.append(resultado)
    return resultado


for i in range(40):
    valor = time.time()
    print(i, fib(i), cont, '%s segundos' % (time.time() - valor))
    cont = 0
