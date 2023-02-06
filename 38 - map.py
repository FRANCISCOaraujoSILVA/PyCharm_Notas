"""
                                                        MAP


- Map: Fazemos o mapeamento de valores para função
- Recebe dois parâmetros. Primeiro: a função. Segundo: um iterável
- Não confundir esse Map com o Mapa estudado em coleções
- Retorna um map object. Mas posso converter
- Só podemos usar uma única vez
"""

import math


def aras(r):
    """
    :param r: raio do círculo
    :return: área
    """
    return math.pi*r**2


print(f'Área do círculo: {aras(2)} u.a')
print(f'Área do círculo: {aras(3.14)} u.a')
print('-----')

# Imagine agora. Uma lista contendo vários raios, como calcular a área de cada um deles? Segue o exemplo abaixo

raios = [2, 3, 5, 20]


# Exemplo 1. Modo convencional, usando do laço for

raio = []
for i in raios:
    raio.append(aras(i))

print(f'Todos os raios a partir da lista de raios: {raio}')
print('-----')

# Exemplo 2. Modo avançado, usando o Map. Recebe a função e o iterável. O map aplica a função em cada dado do iterável

areeas = map(aras, raios)
print(areeas)
print(type(areeas))
print(f'Valores com o map() e transformados em lista: {list(areeas)}')  # Muito mais prático
print('-----')

# A grande sacada, é que geralmente não criamos uma função para isso. Usamos as expressções lambdas direto no map.
# Vamos refatorar nosso problemas:

print(f'A área da nossa função refatorada: {list(map(lambda r: math.pi*r**2, raios))}')  # Muito legal
# Note: lambda r: math.pi*r**2 --> função; raios --> iterável
print('-----')

"""
NOTA IMPORTANTE: 
- Após utilizar a função map(), depois da primeira utilização do resultado, nossos valores são zerados
- Para fixar: Map precisa de uma função e um iterável. Essa função pode ser anônima ou não
"""

# Exemplo com cidade e temperatura em graus celcius

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

# Como podemos passar para graus fahrenheit?

"""
dado: lista de cidades, nesse caso
f = 9/5 * c + 32
"""

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)  # Transformando graus celcius para fahrenheit

print(f'Cidades com as temperaturas convertidas: \n {list(map(c_para_f, cidades))}')  # Esse exemplo foi muito bom
