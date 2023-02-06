"""
                                                    ANY E ALL - FUNÇÕES BOOLEANAS


- Algum e todo
- All(): retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável estiver vazio
- Any(): retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os valores são True, menos o 0 que é False
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True
print(all('Francisco Araújo'))  # True
print('-----')

# Vamos fazer uma busca com list comprehension + all(). Boa combinação para se fazer uma checagem

nomes = ['Carina', 'Carla', 'Clara', 'Catarina', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print('-----')

# Um iterável vazio convertido em booleano é False, mas o all() entende como True. Sempre vai dar True aqui

print(all([letra for letra in 'eio' if letra in 'aeiou']))
print('-----')

# Outro caso. Se for par será True, se for vazio será True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # Para cada número da lista, verifica se é par (True)
print('-----')  # *

# Exemplo com any()

print(any([0, 1, 2, 3, 4]))  # Se existir apenas um verdadeiro, retorna verdadeiro
print(any([]))  # False

nomes = ['Carina', 'Carla', 'Clara', 'Catarina', 'Cassiano', 'Cristina', 'Francisco']
print(any([nome[0] == 'C' for nome in nomes]))  # True
