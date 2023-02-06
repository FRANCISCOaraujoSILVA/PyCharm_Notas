"""
                                        TESTE DE MEMÓRIA COM GENERATORS


- Quando usar GENERATORS? quando queremos ter um baixo consumo de memória!
- Ter baixo consumo de memória não está relacionado com alta velocidade de processamento
"""

# Sequência de fibonacci (usando listas): A lista é gerada toda de uma vez (ocupa mais memória)


def fib_lista(maxi):
    nums = []
    a, b = 0, 1
    while len(nums) < maxi:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100):
    print(n)
# A função fib_lista() usou 450 MB na memória do computador

# Sequência de fibonacci (usando geradores): Geramos  o número um a um (ocupa menos memória)


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(10000):
    print(n)

# A função fib_gen() usou 3,5 MB na memória do computador
