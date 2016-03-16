
def f():
    return 'retorno f'

g=f

f=2

print(g)
print(g())
print(f)