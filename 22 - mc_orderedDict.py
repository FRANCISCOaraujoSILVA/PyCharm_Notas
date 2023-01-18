"""
                                        MÓDULO COLLECTIONS - ORDERED DICT


"""

from collections import OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)
print('-----')

for chave, valor in dicionario.items():  # Nomeando a chave e o valor do dicionário
    print(f'Chave = {chave}: Valor = {valor}')
print('-----')

dictionay = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dictionay.items():
    print(f'Chave = {chave}: Valor = {valor}')
print('-----')

# Entendendo a difereça entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True. A ordem dos elementos NÃO IMPORTA para o dicionário comum
print('-----')

# Ordered Dict

dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'a': 2, 'b': 1})

print(dict3 == dict4)  # False. A ordem dos elementos IMPORTA para o Ordered Dict
