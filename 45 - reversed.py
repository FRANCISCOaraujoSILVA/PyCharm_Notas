"""
REVERSED

Obs.: não confunda com a função reverse() que estudamos nas listas

- A função reverse() é aplicado apenas sobre as listas
- A função reversed é aplicado para qualquer iterável. Ou seja, sua função é inverter um iterável.

"""

# Exemplos
lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
print(type(res))

"Ou seja, a função reversed() retorna um iterável do tipo <class 'list_reverseiterator'>"

# Mas podemos converter este tipo:

# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# set (conjunto), lembrando que em conjuntos, não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()

for letra in reversed('Francisco'):
    print(letra, end='')  # lembrando que o end desabilita a quebra automática de linha

print('\n')  # para pular uma linha

# Podemos fazer sem usar o for
print(''.join(list(reversed('Francisco'))))  # join transforma uma lista de string em uma string
print('-----')
# também podemos usar o slice de string
print('Francisco'[::-1])

print('-----')
# podemos fazer um loop for reverso
for i in reversed(range(0, 10)):
    print(i)

print('-----')
# lembrando que também podemos fazer com o próprio range
for n in range(9, 0, -1):
    print(n)
