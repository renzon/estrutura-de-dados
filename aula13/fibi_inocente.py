import time
from functools import lru_cache

cont = 0


@lru_cache(maxsize=128)
def fib(n):
    global cont
    cont += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


for i in range(40):
    valor = time.time()
    print(i, fib(i), cont, '%s segundos' % (time.time() - valor))
    cont = 0
