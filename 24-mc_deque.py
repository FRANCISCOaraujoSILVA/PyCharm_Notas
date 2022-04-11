"""
MÓDULO COLLECTIONS: DEQUE

Podemos dizer que é uma lista de ALTO DESEMPENHO.
"""
from collections import deque

# Criando deques
deq = deque('Francisco')
print(deq)
print('-----')

# Adicionando elementos
deq.append(' Araújo')  # Da mesmo forma que adicionamos na lista
print(deq)
print('-----')

deq.appendleft('Silva')  # Adiciona no começo da lista. Uma vantagem
print(deq)
print('-----')

# Remover elementos
print(deq.pop())  # remove e retorna o último elemento da lista
print(deq)
print('-----')

print(deq.popleft())
print(deq)
