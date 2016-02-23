lst = [1, 2, 3]
tpl = (1, 2, 3)
s = '123'

primeiro, *t = tpl
print(t)
print(primeiro)

lst[0], lst[1] = lst[1], lst[0]
print(lst[0])
print(tpl[0])
print(s[0])


def f(a, b):
    return a * 2, b * 2


tpl = (1, 2)

a, b = f(*tpl)
print(a, b)
print(type(tpl))
