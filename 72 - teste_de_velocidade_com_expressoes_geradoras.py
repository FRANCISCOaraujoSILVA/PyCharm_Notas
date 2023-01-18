"""
TESTE DE VELOCIDADE COM EXPRESSÕES GERADORAS

"""
"""
# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # generator
print(next(ge1))
print(next(ge1))

print('-----')


# Generation Expression

ge2 = (num for num in range(1, 10))
print(ge2)  # generator expression
print(next(ge2))
print(next(ge2))
"""

# Usando várias funções integradas
print(sum(num for num in range(1, 10)))  # some (número para cada número no range*
# nota: "num for num in range(1, 10)" é uma expressão geradora
print('-----')


# Realizando teste de velocidades
import time

# Generator Expression

gen_inicio = time.time()  # tempo atual
print(sum(num for num in range(100_000)))
gen_tempo = time.time() - gen_inicio
print('-----')
# List Comprehension
list_inicio = time.time()  # tempo atual
print(sum([num for num in range(100_000)]))  # veja os colchetes do list comprehension
list_tempo = time.time() - list_inicio
print('-----')

print(f'Tempo de Generators Expression: {gen_tempo} s')  # mais veloz
print(f'Tempo de List Comprehension: {list_tempo} s')  # menos veloz
