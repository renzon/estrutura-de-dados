from array import array

vetor = array('i', [1, 2, 3,4])
vetor[0]=9
print(id(vetor[0]))
print(id(vetor[1]))
print(id(vetor[2]))
print(id(vetor[0]))
print(id(vetor[1]))
print(id(vetor[2]))
print(id(vetor[3]))
