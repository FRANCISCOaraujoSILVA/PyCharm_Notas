"""
                                                        *ARGS


- Entendendo o *args: Um parâmetro especial de funções
- *args: parâmetro de entrada, como qualquer outro. Significa que você poderá chamá-lo de qualquer nome, desde de que
comece com asterisco

O que é o *args?
    - É usado em funções e coloca os valores extras (informado nos parâmetros) em uma tupla. Ou seja, imutáveis!
    - O argumento nõa é obrigatório
    - Naturalmente, o '*' desempacota os dados


Nota:
O *args transforma os dados em tuplas, mas gera erro ao transformar tupla em tupla.
"""

# Exemplo 1: Limitado, não trabalha além dos 3 argumentos


def soma_todos(num1, num2, num3):
    return num1+num2+num3


print(soma_todos(1, 2, 3))  # OK
# print(soma_todos(1, 2))  # OK, se existisse parâmetro padrão
# print(soma_todos(1, 2, 3, 6))  # TypeError, mesmo se existir parâmetro padrão
print('-----')

# Exemplo 2: Entendendo o *args


def soma_todos_novamente(*args):  # Com asterisco
    print(sum(args))  # Sem asterisco


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
print('-----')

# Ou


def depois_soma(*args):
    return sum(args)


print(depois_soma())
print(depois_soma(1, 2))
print(depois_soma(1, 2, 3))
print(depois_soma(1, 2, 3, 4))
print('-----')

# Outro exemplo


def verifica_inf(*args):
    if 'Francisco' in args and 'Araújo' in args:
        return 'Bem vindo Francisco'
    return 'Não tenho certeza de quem você é!'


print(verifica_inf())
print(verifica_inf(1, True, 'Francisco', 'Araújo'))
print(verifica_inf(1, 'Araújo', 2.71))
print('-----')

# Como resolver problema seguinte ao somar elementos de uma lista em um args?


def somando(*args):
    return sum(args)


# Desempacotador para resolver o problema do TypeError abaixo. Vamos fazer automaticamente

"""
- Modo antigo: num1, num2, num3, num4 = numeros
- Modo moderno: *numeros

O asterisco indica que estamos passando uma coleção e que essa coleção precisa ser desempacotada.
Até o momento, podemos desempacotar conjunto, lista e até a própria tupla. Mas ainda não podemos desempacotar um dict.
"""

numeros = (1, 2, 2,)
print(somando(*numeros))  # Sem o asterisoco gera um TypeError. Gostei desse método

# Meu exemplo 😉


def mensagem(*args, nome='Francisco', sobrenome='Araújo'):
    return f'Olá {nome} {sobrenome} Seu número da sorte é {sum(args)}'


num = [1, 2, 3]
print(mensagem(*num, nome='Larissa'))
