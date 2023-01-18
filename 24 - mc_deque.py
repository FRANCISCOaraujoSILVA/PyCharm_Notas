"""
                                        MÓDULO COLLECTIONS - DEQUE

- Podemos dizer que é uma lista de ALTO DESEMPENHO
"""

from collections import deque

# Criando deques

deq = deque('Francisco')
print(deq)
print('-----')

# Adicionando elementos

deq.append(' Araújo')  # Da mesma forma que aprendemos na lista
print(deq)
print('-----')

deq.appendleft('Silva')  # Adiciona no começo da lista. Uma vantagem
print(deq)
print('-----')

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento da lista, lembra?
print(deq)
print('-----')

print(deq.popleft())
print(deq)
