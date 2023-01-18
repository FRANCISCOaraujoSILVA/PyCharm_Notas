"""
                ENTENDENDO E EXPLORANDO RANGES - NÃO É UM LAÇO DE REPETIÇÃO, É MAIS UMA FUNÇÃO AUXILIAR


- Precisamos conhecer o loop for para usar bem os ranges
- Precisamos conhecer o range para trabalhar melhor com loop for
- Ranges são utilizados para gerar sequências numéricas, nõo de forma aleatória, mas sim de maneira específica
"""

# Formas gerais

"""
# Forma 1:
range(valor_de_parada)
Obs.: valor_de_parada não inclusivo (início padrão em 0 e passo de 1 em 1)
"""

for num in range(12):  # Indo de 0 até 12-1
    print(num)
print('-----')

"""
# Forma 2:
range(valor_de_início, valor_de_parada)
Obs.: valor_de_parada não inclusivo (início padrão especificado e passo de 1 em 1)
"""

for num in range(2, 12):
    print(num)
print('-----')

"""
# Forma 3:
range(valor_de_início, valor_de_parada, passo)
Obs.: valor_de_parada não inclusivo (início padrão específicado e passo especificado)
"""

for num in range(0, 20, 4):
    print(num)
print('-----')

"""
# Forma 4:
igual a três, mas inversa.
range(valor_de_início, valor_de_parada, -passo)
"""

for num in range(20, 0, -1):
    print(num)

# Obs.: Para criar uma lista (a partir do range) no terminal, basta fazer: lista = list(range(12))

lista = list(range(20))
print(f'Tipo de dado: {type(lista)}')
print(f'Criado a partir do range e depois transformado em uma lista: {lista}')
