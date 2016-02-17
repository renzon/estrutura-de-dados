cont=0


def hanoi(n, ori='A', dest='B', aux='C'):
    global cont
    cont += 1
    if n == 1:
        print('%s -> %s' % (ori, dest))
    else:
        hanoi(n - 1, ori, aux, dest)
        print('%s -> %s' % (ori, dest))
        hanoi(n - 1, aux, dest, ori)


for i in range(1, 5):
    print('###### solução %s' % i)
    cont=0
    hanoi(i)
    print('Tempo de execução %s'% cont)

