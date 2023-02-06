"""
                                        ENTENDENDO ITERATORS E ITERABLES


Iterator:
    - Um objeto da programção que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada
Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada
"""

# Exemplos de iterable

nome = 'Francisco'
numeros = [1, 2, 3, 4, 5, 6]
# print(next(nome))  # Vai gerar uma erro, pois não é iterator, é iterable
# print(next(numeros))  # Vai gerar uma erro, pois não é iterator, é iterable

# Podemos transfomar um iterable em um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # F
print(next(it1))  # r
print(next(it1))  # a
print(next(it1))  # n
print(next(it1))  # c
print(next(it1))  # i
print(next(it1))  # s
print(next(it1))  # c
print(next(it1))  # o
print('-----')

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print('-----')

# Por baixo dos panos, é isso o que acontece

nome = 'Francisco'
numeros = [1, 2, 3, 4, 5, 6]
for letra in nome:
    print(f'{letra}')
print('-----')

"""
Veja que por baixo dos panos o laço for verifica a variável 'nome', reconhe que é um 'iterable', aplica o iter() e 
depois o next(). O next() é na verdade o print sendo aplicado no laço for.
"""
