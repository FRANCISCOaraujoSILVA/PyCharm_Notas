"""
                                                            REVERSED


- Não confunda com a função reverse() que estudamos nas listas
- A função reverse() é aplicado apenas sobre as listas
- Já a função reversed() é aplicado sobre qualquer iterável. Ou seja, sua função é inverter um iterável
"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))  # A função reversed() retorna um iterável do tipo <class 'list_reverseiterator'>

# Mas podemos converter este tipo

# Para lista

print(list(reversed(lista)))

# Para tupla

print(tuple(reversed(lista)))

#  Pra um set (conjunto). Lembrando que em conjuntos, não definimos a ordem dos elementos

print(set(reversed(lista)))
print('-----')

# Podemos iterar sobre o reversed()

for letra in reversed('Francisco'):
    print(letra, end='')  # Lembrando que o end desabilita a quebra automática de linha

print('\n')  # Para pular uma linha

# Podemos fazer sem usar o for

print(''.join(list(reversed('Francisco'))))  # Join transforma uma lista de string em uma string
print('-----')

# Também podemos usar o slice de string

print('Francisco'[::-1])
print('-----')

# Podemos fazer um loop for reverso

for i in reversed(range(0, 10)):
    print(i)
print('-----')

# Lembrando que também podemos fazer com o próprio range

for n in range(9, 0, -1):
    print(n)
