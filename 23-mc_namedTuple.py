"""
MÓDULO COLLECTIONS: NAMED TUPLE

Named Tuple: são tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""
from collections import namedtuple
# Precisamos definir o nome e parâmentros
# Forma 1 - Declaração Named Tuple
cachorro1 = namedtuple('cachorro', 'idade raca nome')  # O primeiro argumento é o nome da tupla

# Forma 2 - Declaração Named Tuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple. Esta forma é mais recomendada. Fica mais claro visualmente. Importante, top
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Utilizando
# Forma 1 - Recomendado
Apoll = cachorro3(idade=1, raca='vira-Lata', nome='Apollo')
print(Apoll)
print(Apoll[0])  # idade
print(Apoll[1])  # raça
print(Apoll[2])  # nome

# Forma 2. Modo recomendado
print('-----')
print(Apoll.idade)
print(Apoll.raca)
print(Apoll.nome)

# Lembrando da aula de tupla:

print('-----')
print(Apoll.index('Apollo'))  # Índice do elemento na tupla
print(Apoll.count('Apollo'))  # Ocorrencias do valor na tupla
