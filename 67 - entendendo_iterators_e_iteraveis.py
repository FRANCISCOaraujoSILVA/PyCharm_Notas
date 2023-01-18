"""
ENTENDENDO ITERATORS E ITERABLES


Iterator:
    - um objeto da programção que pode ser iterado
    - um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable:
    - um objeto que irá retornar um iterator quando a função iter() for chamada
"""
# exemplos de iterable
nome = 'Francisco'
numeros = [1, 2, 3, 4, 5, 6]

# print(next(nome)) # vair gerar uma erro, pois não é iterator
# print(next(numeros))

# podemos transfomar um iterable em um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print('-----')
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print('-----')
# Por baixo dos panos
for letra in nome:
    print(f'{letra}')

"""
Veja que por baixo dos panos o laço for verifica a variável 'nome', reconhe que é um 'iterable',
 aplica o iter() e depois o next(). O next() é na verdade o print sentdo aplicado no laço.
"""
