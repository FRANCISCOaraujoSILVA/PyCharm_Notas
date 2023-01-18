"""
GENERATORS EXPRESSION:

Possui muita performance, confirme com os resultados a baixo.
Generators: Vai gerar um objeto em memória, ou seja, posso mudar o estilo do dado
    - Podemos usar os dados apenas uma vez, assim como map, filter...
    - Possui muito mais performance
Já vimos;
    - list comprehensionc, já gera lista em memória
    - dictionary comprehension, já gera dicionário em memória
    - set comprehension, já gera conjunto em memória

Não vimos;
    - tuple comprehension, pois elas sãos os chamados  GENERATORS

Na aula passado foi feito:
nomes = ['Carina', 'Carla', 'Clara', 'Camilha', 'Cassiano', 'Cristina', 'Francisco']
print(any([nome[0] == 'C' for nome in nomes]))  # True

Obs.: Poderíamos fazer usando generators.
Portanto, é recomendado usar o generators na maioria dos casos, a não ser que queiramos um conjuta, um dicionáiro ou
uma lista logo de cara.
"""
# Qual a utilidade de getsizeof()? - Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof
print(getsizeof('Francisco Araújo'))
print(getsizeof(9))
print(getsizeof(96356525653256))
print(getsizeof(True))
print('-----')

# lista de números usando o list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(f'Bytes em list comprehension: {list_comp}')
print('-----')
# lista de números usando o set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
print(f'Bytes em set comprehension: {set_comp}')
print('-----')
# lista de números usando o dictionary comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f'Bytes em dic comprehension: {dic_comp}')
print('------')
# lista de números usando o generators
gen = getsizeof(x * 10 for x in range(1000))
print(f'Veja como temos menos bytes em Generator Expression: {gen}')
print('-----')

# Usando generators
nomes = ['Carina', 'Carla', 'Clara', 'Camilha', 'Cassiano', 'Cristina', 'Francisco']
print(any((nome[0] == 'C' for nome in nomes)))  # Veja que agora é um tuple comprehension (generators).
# Vai gerar performance
print('-----')

"""
Por que o generator usa tão pouco bytes em memória?
Porque ele ainda não gerou nada, só deixou tudo preparado, e quando for usar vai gerar em memória e apagar em memória, 
diferente do lis comprehension
"""

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)



