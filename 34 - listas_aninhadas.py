"""
                                                    LISTAS ANINHADAS


Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays (MatLab por exemplo):
    - Unidimensionais (arrays/vetores)
    - Multidimensionais (matrizes)

Em Python temos as listas:
    - numeros = [1, 'b', 3.14, 4, True, 6]
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))
print('-----')

# Como acessar os dados?

print(listas[0][2])  # Acessando a linha 1, coluna 3 da matriz
print(listas[2][1])  # Acessando a linha 3, coluna 2 da matriz
print(listas[2][-2])  # Acessando a linha 3, coluna 2 da matriz. Esse modo é interessante
print('-----')

# Iterando com loops em uma lista aninhada. Vamos precisar de dois loops

for lista in listas:  # Temos 3 listas na matriz 3x3
    for num in lista:  # itera em cada lista da matriz 3x3
        print(f'O número com o for: {num}')

# Muito mais fácil do que no matlab. Isso é alegria 😉
print('-----')


# Como usar List Comprehension nesse caso? Segue o exemplo abaixo

# 1° [[] for lista in listas]
# 2° [[for valor in lista] for lista in listas]
# 3° [[print(valor) for valor in lista] for lista in listas]
[[print(f'O valor com list comprehension: {valor}') for valor in lista] for lista in listas]
print('-----')

# Gerando uma matriz 3x3

print(f'A matriz: {[[numero for numero in range(1, 4) ] for valor in range(1, 4)]}')
print(f'A matriz: {[[numero for numero in [6, 7, 2] ] for valor in [1, 3, 4]]}')  # Uma forma diferente

""" 
Primeiro preencheu colunas com o "valor", depois preencheu as linhas com o "numero".
"""
print('-----')

# Jogo da velha. Vamos usar a estrutura condicional

a = [['x' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
# Ou seja, preencher com um 'x' se o número contido na matriz for par
print(f'O jogo da velha: {a}')
print('-----')

# Gerando valores iniciais

print(f"Com valores inciais: {[['*' for val in range(1, 4)] for nu in range(1, 4)]}")
