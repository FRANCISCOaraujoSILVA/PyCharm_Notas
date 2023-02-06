"""
                                FUNÇÕES DE MAIOR GRANDEZA (HIGHER ORDER FUNCTIONS - HOF)


- O que isso significa?
    - Quando uma linguagem de programação suporta HOF indica que podemos ter funções que retornam outras funções como
    resultado, ou mesmo que podemos passar funções como argumento para outras funções e até mesmo criar variáveis do
    tipo funções em nossos programas

Obs.: Na seção de funções, já utilizamos (sem saber) isso.

- Em Python, as funções são cidadãos de primeira classe
- Os decoradores em Python nos ajudam a adicionar comportamento ao nosso código
"""

from random import choice

# Exemplo: Definindo as funções (normalmente)


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)  # Estamos retornando a execução da função


# Testando as funções

print(f' A soma: {calcular(4, 2, somar)}')
print(f' A Subração: {calcular(4, 2, diminuir)}')
print(f' A multiplicação: {calcular(4, 2, multiplicar)}')
print(f' A divisão: {calcular(4, 2, dividir)}')
print('-----')


# Nested Functions - Funções Aninhadas

"""
Em Python, podemos ter funções dentro de funções (Nested Functions ou Inner Functions)
"""

# Exemplo


def cumprimento(pessoa):

    def humor():  # Função interna (função aninhada - função dentro de função)
        return choice(('E ai, ', 'Suma daqui! ', 'Gosto muito de você...♥ '))
        # Choice: seleciona, aleatoriamente, um dos elementos
    return humor() + pessoa  # Estamos executando a função, observe os parênteses

# Testando


print(cumprimento('Francisco'))
print(cumprimento('Anna'))
print('-----')


# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahah ', 'kkkkkkkkkkk ', 'yayayayayayay '))
    return rir  # Veja que estamos retornando a função, e não a execução da função - sem os parênteses


# Testando

rindo = faz_me_rir()
print(rindo())
print('-----')

"""
Conclusões: 
- Inner Functions podem acessar o escopo de funções mais externas
- A função humor() poderia acessar o escopo da função cumprimento()
- A função rir() poderia acessar o escopo da função faz_me_rir()
"""

# Exemplo


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahah ', 'kkkkkkkkkkk ', 'yayayayayayay '))
        return f'{risada} {pessoa}'
    return dando_risada   # Estamos apenas retornando a função, e não executando - sem os parênteses


# Testando

rindo = faz_me_rir_novamente('Francisco')  # A variável recebe a execução da função
print(rindo())  # Estamos executando a variável como se fosse a função
print(rindo())
