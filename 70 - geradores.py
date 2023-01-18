"""
GERADORES

- Geradores (generators) são iteradores (iterators)
    - Obs.: A recíproca não é verdadeira, nem todo iterators é um generator
- Generators podem ser criados com funçõe geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com expressões geradoras


Diferenças entre Funções e Generator Functions;
 ..............................................................................
|FUNÇÕES                             |GENERATORS FUNCTIONS                    |
-------------------------------------------------------------------------------
|utlizam retur                       |utilizam yield                          |
-------------------------------------------------------------------------------
|retona uma vez, ou none             |podem utilizar yield múltiplias vezes   |
-------------------------------------------------------------------------------
|quando executada, retorna um valor  |quando executada, reotorna um generator |

"""
# Exemplo de Generators Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # yiel, é com se fosse o return, ele retorna contador.
        contador = contador + 1


"""
Nota: lembre-se, o return finaliza a função, já o yiel não encerra a função, ele fica esperando o próximo next().
Um GENERATOR FUNCTION não é um GENERATOR. Ele gera um GENERATOR.
"""
# 1
gen = conta_ate(5)
# print(type(gen)) # <class 'generator'>
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # 4
# print(next(gen))  # 5


# 2
# print(next(gen))  # 1
# print('-----')
# for num in gen:  # começa a partir do 2, gerar um por vez
#    print(num)


# 3 para gerar todos de uma vez
print(list(conta_ate(6)))
