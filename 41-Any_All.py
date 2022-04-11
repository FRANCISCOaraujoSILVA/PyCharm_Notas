"""
ANY E ALL:

algum e todo
Any e all
All(): retorna True (booleano) se todos os elementos do iterável são verdadeiros ou ainda se o iterável estiver vazio.
Uma função booleana

any(): retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # todos os valores são True, menos o 0. False
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True
print(all('Francisco Araújo'))  # True
print('-----')


# Vamos fazer uma busca com list comprehension + all(). Bom para se fazer uma checagem
nomes = ['Carina', 'Carla', 'Clara', 'Camilha', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print('-----')

# Um iterável vazio convertido em booleano é False, mas o all() entende como True. Sempre vai dar True aqui.
print(all([letra for letra in 'eio' if letra in 'aeiou']))
print('-----')

# outro caso, e for par vai da True, se for vazio vai dar True
print(all([num for num in [4, 2, 10, 6, 8] if num % 1 == 0]))
print('-----')

# Exemplo com any()
print(any([0, 1, 2, 3, 4]))  # se tiver apenas um verdadeiro, retorna verdadeiro.
print(any([]))  # False

nomes = ['Carina', 'Carla', 'Clara', 'Camilha', 'Cassiano', 'Cristina', 'Francisco']
print(any([nome[0] == 'C' for nome in nomes]))  # True
print('-----')
