"""
                                TESTE DE VELOCIDADE COM EXPRESSÕES GERADORAS


"""

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # Generator
print(next(ge1))  # 1
print(next(ge1))  # 2
print('-----')

# Generation Expression

ge2 = (num for num in range(1, 10))
print(ge2)  # Generator expression
print(next(ge2))  # 1
print(next(ge2))  # 2
print('-----')

# Usando várias funções integradas

print(sum(num for num in range(1, 10)))  # Soma (número para cada número no range())
# Nota: "num for num in range(1, 10)" é uma expressão geradora
print('-----')

# Realizando teste de velocidades

import time

# Generator Expression

gen_inicio = time.time()  # Tempo atual
print(sum(num for num in range(100_000)))
gen_tempo = time.time() - gen_inicio
print('-----')
# List Comprehension
list_inicio = time.time()  # Tempo atual
print(sum([num for num in range(100_000)]))  # Veja os colchetes do list comprehension
list_tempo = time.time() - list_inicio
print('-----')

print(f'Tempo de Generators Expression: {gen_tempo} s')  # Mais veloz
print(f'Tempo de List Comprehension: {list_tempo} s')  # Menos veloz
