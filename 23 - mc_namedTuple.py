"""
                                        MÓDULO COLLECTIONS - NAMED TUPLE


Named Tuple: São tuplas diferenciadas onde especificamos um nome para a mesma e também para seus parâmetros
"""

from collections import namedtuple

# Precisamos definir o nome e os parâmentros

# Forma 1: Declaração Named Tuple

cachorro1 = namedtuple('cachorro', 'idade raca nome')  # O primeiro argumento é o nome da tupla

# Forma 2: Declaração Named Tuple

cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3: Declaração Named Tuple. Esta forma é mais recomendada. Fica mais claro visualmente. Importante, top

cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Utilizando

# Forma 1: Recomendado

Apoll = cachorro3(idade=1, raca='vira-Lata', nome='Apollo')
print(Apoll)
print(Apoll[0])  # idade
print(Apoll[1])  # raça
print(Apoll[2])  # nome
print('-----')

# Forma 2: Modo recomendado

print(Apoll.idade)
print(Apoll.raca)
print(Apoll.nome)
print('-----')

# Lembrando da aula de tupla

print(Apoll.index('Apollo'))  # Índice do elemento 'Apollo' na tupla
print(Apoll.count('Apollo'))  # Ocorrências do valor 'Apollo' na tupla
