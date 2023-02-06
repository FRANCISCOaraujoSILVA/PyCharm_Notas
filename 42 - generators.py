"""
                            GENERATORS EXPRESSION - TAMBÉM CONHECIDO COMO TUPLE COMPREHENSION


 - Possui alta performance, confirme com os resultados a baixo

Generators: Gera um objeto em memória, ou seja, posso mudar o estilo do dado
    - Podemos usar os dados apenas uma vez, assim como o map, filter...
    - Possui muito mais performance
Já vimos:
    - List comprehension, gera lista em memória
    - Dictionary comprehension, gera dicionário em memória
    - Set comprehension, já gera conjunto em memória
Não vimos:
    - Tuple comprehension, os chamados GENERATORS

Na aula passado foi feito:
    nomes = ['Carina', 'Carla', 'Clara', 'Catarina', 'Cassiano', 'Cristina', 'Francisco']
    print(any([nome[0] == 'C' for nome in nomes]))  # True

Nota:
- Poderíamos solucionar o mesmo problema usando generators
- É recomendado usar o generators na maioria dos casos, a não ser que queiramos um conjuto, um dicionário ou uma lista
logo de cara
"""

# Qual a utilidade de getsizeof()? - Retorna a quantidade de bytes em memória do elemento passado como parâmetro

from sys import getsizeof

print(getsizeof('Francisco Araújo'))
print(getsizeof(9))
print(getsizeof(96356525653256))
print(getsizeof(True))
print('-----')

# Lista de números usando o list comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])
print(f'Bytes em list comprehension: {list_comp}')
print('-----')

# Lista de números usando o set comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})
print(f'Bytes em set comprehension: {set_comp}')
print('-----')

# Lista de números usando o dictionary comprehension

dic_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f'Bytes em dic comprehension: {dic_comp}')
print('------')

# Lista de números usando o generators
gen = getsizeof(x * 10 for x in range(1000))
print(f'Veja como temos menos bytes em Generator Expression: {gen}')
print('-----')

# Usando generators

nomes = ['Carina', 'Carla', 'Clara', 'Catarina', 'Cassiano', 'Cristina', 'Francisco']
print(any((nome[0] == 'C' for nome in nomes)))  # Veja que agora é um tuple comprehension (generators). Gera performance
print('-----')

"""
Por que o generator usa tão pouco bytes em memória?
Porque ele ainda não gerou nada, só deixou tudo preparado, e quando for usar vai gerar em memória e apagar em memória, 
diferente do lis comprehension.
"""

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))
print(' ')
print(f'{getsizeof(gen)} bytes')
print(' ')

for num in gen:
    print(num)
