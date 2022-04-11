"""
ARGS:

Entendendo o *args: Um parâmetro especial de funções
*args: parâmetro de entrada, como qualquer outro. Significa que você poderá chamá-lo de qualquer nome, desde de que
comece com asterisco

O que é o *args?
- é utilizado em uma função e coloca os valores extras informados como entrada em uma tupla. Ou seja, imutáveis! já
que é uma tupla ou vai será transformada em tupla.
- o argumento nõa é obrigatório
- naturalmente, o * desempacota
Obsrvação pessoal. Ele transforma os dados em tuplas, mas gera erro ao transformar tupla em tupla.
"""
# Exemplo 1 - não trabalha além dos 3 argumentos, mesmo com argumento padrão, e teríamos que trabalhar com o return...


def soma_todos(num1, num2, num3):
    return num1+num2+num3


print(soma_todos(1, 2, 3))  # ok
# print(soma_todos(1, 2))  # Ok se existir parâmetro padrão
# print(soma_todos(1, 2, 3, 6))  # TypeError, mesmo se existir parâmetro padrão


print('-----')
# Exemplo 2 - Entendendo o *args


def soma_todos_novamente(*args):  # Com asterisco
    print(args)  # sem asterisco


soma_todos_novamente()
soma_todos_novamente(1)
soma_todos_novamente(1, 2)
soma_todos_novamente(1, 2, 3)
print('-----')


# Refatorando


def soma_agora(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_agora())
print(soma_agora(1, 2))
print(soma_agora(1, 2, 3))
print(soma_agora(1, 2, 3, 4))


# or
print('-----')


def depois_soma(*args):
    return sum(args)


print(depois_soma())
print(depois_soma(1, 2))
print(depois_soma(1, 2, 3))
print(depois_soma(1, 2, 3, 4))


# Outro exemplo
def verifica_inf(*args):
    if 'Francisco' in args and 'Araújo' in args:
        return 'Bem vindo Francisco'
    return 'Não tenho certeza de quem você é!'


print(verifica_inf())
print(verifica_inf(1, True, 'Francisco', 'Araújo'))
print(verifica_inf(1, 'Araújo', 2.71))


# Como resolver esse problema ao somar elementos de uma lista em um args?
print('-----')


def somando(*args):
    return sum(args)


# Desempacotador para resolver o problema do TypeErro abaixo. Vamos fazer automaticamente.
"""
Modo antigo: num1, num2, num3, num4 = numeros / modo moderno: *numeros
O asterisco indica que estamos passando uma coleção e que precisa ser desempacotado
Até o momento, podemos desempacotar conjunto, lista e até a própria tupla. Mas ainda não podemos desempacotar um dict.
"""
numeros = (1, 2, 2,)
print(somando(*numeros))  # sem o asterisoco gera um TypeError

# Meu exemplo :-)


def mensagem(*args, nome='Francisco', sobrenome='Araújo'):
    return f'Olá {nome} {sobrenome} Seu número da sorte é {sum(args)}'


num = [1, 2, 3]
print(mensagem(*num, nome='Larissa'))
