def minmax(l):
    if len(l)==0:
        return None,None
    if len(l)==1:
        return l[0],l[0]
    else:
        return MaxMin(l,len(l),l[0],l[0])

def MaxMin(l,t,mi,ma):
    if mi>l[t-1]:
        mi=l[t-1]
    if ma<l[t-1]:
        ma=l[t-1]
    if t==1:
        return mi,ma
    else:
        return MaxMin(l,t-1,mi,ma)

print(minmax([1,2]))

'''
tempo O(n) pois vai percorrer a lista inteira.
Memória O(n)
'''