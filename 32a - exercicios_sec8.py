"""
                  ///Espaço reservado para solucionar alguns exercícios da seção 8///
"""

import math

# 1


def func(numero):
    return numero * 2


print(func(10))
print('-----')

# 2


def horario(dia, mes, ano):
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    return f'{dia} de {meses[mes-1]} de {ano}'


print(horario(1, 12, 2022))
print('-----')

# 3


def avalia(numero):
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    return 1


print(avalia(0))
print('-----')

# 4


def verifica(numero):
    if numero < 0:
        return f'{numero} é um número negativo, não poderá ser quadrado perfeito!'
    elif numero == 0:
        return f'{numero} não é um quadrado perfeito!'
    else:
        if numero**(1/2) == int(numero**(1/2)):
            return f'{numero} é um quadrado perfeito!'
        return f'{numero} não é um quadrado perfeito!'


print(verifica(9))
print('-----')

# 5


def volume(raio):
    return f'Volume da esfera: {(4/3)*math.pi*raio**2} u.v'


print(volume(2))
print('----')

# 8


def raiz(ca, co):
    return f'Valor da hipotenusa = {math.sqrt(ca**2+co**2)}'


print(raiz(2, 2))
print('-----')

# 10


def tipo(a, b):
    tip = [a, b]
    return f'O maior: {max(tip)}'


print(tipo(5, 4))
print('-----')

# 11


pesos = [5, 3, 2]
somando = 0


def analisa(a, b, c, *args):
    global pesos
    global somando
    listanota = [a, b, c]
    if args[0] == 'A' or args[0] == 'a':  # [0]
        soma = a+b+c
        return f'A média aritmética: {soma/(len(pesos))}'
    elif args[0] == 'P' or args[0] == 'p':
        for numero in range(0, len(pesos)):
            somando += pesos[numero] * listanota[numero]
    return f'A média ponderada: {somando/sum(pesos)}'


print(analisa(1, 2, 3, 'a'))
print(analisa(1, 2, 3, 'P'))
print('-----')

# 13


def realiza(a, b, *args):
    if args[0] == '+':
        return f'Soma: {a+b}'
    elif args[0] == '-':
        return f'Subtração: {a-b}'
    elif args[0] == '/':
        return f'Divisão: {a/b}'
    elif args[0] == '*':
        return f'Multiplicação: {a*b}'
    return f"Escolha '+' para adição, '-' para subtração, '/' para divisão ou '*' para multiplicação"


print(realiza(1, 2, '+'))
print(realiza(1, 2, '-'))
print(realiza(1, 2, '/'))
print(realiza(1, 2, '*'))
