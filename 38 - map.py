"""
MAP:

A função do map recebe um parâmetro
Map: Fazemos mapeamento de valores para função.
Não confundir esse Map com o Mapa estudado em coleções
Map: recebe dois parâmetros. Primeiro; a função. Segundo; um iterável
Retorna um map object. Mas posso converter
Só podemos usar uma única vez
A função do Map recebe apenas um parâmetro. Isto é importante.
"""

import math


def aras(r):
    """
    :param r: raio do círculo
    :return: área
    """
    return math.pi*r**2


print(f'A áreia do círculo: {aras(2)} u.a')
print(f'A áreia do círculo: {aras(3.14)} u.a')
print('-----')

# Imagine agora. Uma lista contendo vários raios:
raios = [2, 3, 5, 20]

"""
Primeiro: Calculando todos os raios 
"""
raio = []
for i in raios:
    raio.append(aras(i))


print(f'Todos os raios a partir da lista de raios: {raio}')
print('-----')

"""
Segunda forma. Usando o Map. Essa função vai usar cada função do iterável e aplicar na função. Por isso recebe 
dois parâmentros
"""

areeas = map(aras, raios)
print(areeas)
print(type(areeas))
print(f'Valores transformados em lista: {list(areeas)}')  # muito mais prático
print('-----')

# A grande sacada, é que geralmente não criamos uma função para isso. Usamos as expressções lambdas direto no map.
# Vamos refatorar nosso problemas:
print(f'A área da nossa função refatorada: {list(map(lambda r: math.pi*r**2, raios))}')
print('-----')

"""
NOTA IMPORTANTE: 
Após utilizar a função map(), depois da primeira utilização do resultado nossos valores são zerados

Para fixar: Map precisa de uma função ou um iterável. Essa função pode ser anônima or não.
"""

# Exemplo com cidade e temperatura em graus celcius

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

# como podemos passar para gruas fahrenheit?
"""
dado: lista de cidades, nesse caso
f = 9/5 * c + 32
"""

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(f'Cidades com as temperaturas convertidas:\n {list(map(c_para_f, cidades))}')

# Esse exemplo foi muito bom.
