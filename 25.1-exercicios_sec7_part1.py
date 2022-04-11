"""
Espaço reservado pra solucionar os exercícios da seção 7 - parte 1
"""
"""
# 1
A = [1, 2, 3, 4, 5, 6]
print(A)
print('-----')
# a)
A.extend([1, 0, 5, -2, -5, 7])
print(A)
print('-----')

# b
print(f'A somas dos valores: {sum([A[0], A[1], A[5]])}')
print('-----')

# c
A.insert(4, 100)
print(A)
print('-----')

# d
for valor in A:
    print(f'Cada elemento da lista: {valor}')


# 3
reais = list([])
while len(reais) < 8:
    reais.append(float(input('Digite o próximo valor real para armazena na lista real: ')))

print(f'Os valores reais escolhidos: {reais}')
reais_quadrados = reais.copy()
quadrados = list([])
for i in reais_quadrados:
    quadrados.append(i**2)
print(f'Os valores reais ao quadrado: {quadrados}')
print('-----')
print(reais)
print(quadrados)


# 7
vetor = [1, 3, 4, 5, 8, 8, 10, 19, 34, 23]
maior = max(vetor)
print(f'O maior valor: {maior}\nEstá no índice: {vetor.index(maior)}')
"""
"""
# 14 - Esse é um desafio a se pensar
vetor = [1, 3, 4, 5, 8, 8, 1, 19, 34, 3]
valores_iguais = list([])
for i in vetor:


print(valores_iguais)
"""
