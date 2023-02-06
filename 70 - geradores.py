"""
                                                        GERADORES


- Geradores (generators) são iteradores (iterators)
    - Obs.: A recíproca não é verdadeira, nem todo iterator é generator
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com expressões geradoras

Diferenças entre Funções e Generator Functions;
 ..............................................................................
|FUNÇÕES                             |GENERATORS FUNCTIONS                    |
-------------------------------------------------------------------------------
|utilizam return                     |utilizam yield                          |
-------------------------------------------------------------------------------
|retona uma vez, ou none             |podem utilizar yield múltiplias vezes   |
-------------------------------------------------------------------------------
|quando executada, retorna um valor  |quando executada, retorna um generator  |
 .............................................................................

"""

# Exemplo de Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # yield, é como se fosse o return, ele retorna contador
        contador = contador + 1


"""
Nota: 
Lembre-se, o return finaliza a função, já o yield não encerra a função, ele fica esperando o próximo next().
Um GENERATOR FUNCTION não é um GENERATOR. Ele gera um GENERATOR. Parece confuso? Calma aí.
"""

# 1

gen = conta_ate(5)

# print(type(gen))  # <class 'generator'>
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # 4
# print(next(gen))  # 5
# print('-----')

# 2

print(next(gen))  # 1
print('-----')

for num in gen:  # Um next() já foi dado, agora vai começar a partir do 2. Gera um por vez
    print(num)
print('-----')

# 3: Para gerar todos de uma vez

print(list(conta_ate(6)))
