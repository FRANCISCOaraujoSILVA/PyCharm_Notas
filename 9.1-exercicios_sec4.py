"""
Espaço reservado pra solucionar os exercícios da seção 4
"""
# 1 - Faça um program que leia um número inteiro e o imprima.
# a = input('Digite um número inteiro: ')
# print(f'O número inteiro é: {a}')
print('-----')

# 2 - Faça um programa que leia um número real e o imprima.
b = 2.2
print(f'O número real é: {b}')
print('-----')

# 3 - Peça ao usuário para inserir três números inteiros e imprima a soma deles.
# c = input('informe o primeiro número inteiro: ')
# d = input('informe o segundo número inteiro: ')
# e = input('informe o terceiro número inteiro: ')
# print(f'A soma dos três números inteiros é: {int(c)+int(d)+ int(e)}')
# print(f'A soma dos três números inteiros é: {c+d+e}')  # veja que aqui não estamos somando, estamos concatenando os n°
# lembrar também que sem os "int" o dado é tipo string, devido ao input
print('-----')

# 4 - Leia um número real e imprima o resultado do quadrado desse número.
f = 3
print(f'O quadrado do número real é: {f**2}')
print('-----')

# 5 - Leia um número real e imprima a quinta parte desse número.
g = 5
print(f'A quinta parte do número {g} é: {(1/5)*g}')
print('-----')

# 6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F=C*(9/5)+32, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius.
h = 42
print(f'A temperatura de {h} graus Celsius equivale a {h*(9/5)+32} graus Fahrenheit.')
print('-----')

# 7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = 5*(F - 32)/9, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit
i = 107.6
print(f'A temperatura de {i} graus Fahrenheit equivale a {5*(i-32)/9} graus Celsius.')
print('-----')

# 28
valor1 = 10
valor2 = 20
valor3 = 30
print(f'A soma dos quadrados dos três valores: {(valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)}')
print('-----')

# 43
valor_lido = 425
print(f'Valor total a pagar com 10% de desconto: {valor_lido * .9} R$')
print(f'Valor parcelado, 3x sem juros: {valor_lido/3} R$')
print(f'Comissão do vendedor na compra a vista: {.05 * (valor_lido * .9)} R$')
print(f'Comissão do vendedor na compra parcelada: {.05 * valor_lido}')
print('----')

# 45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver.
j = 'FRANCISCO ARAujo'
print(j.lower())
print('-----')

# 46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado
# pelos dígitos invertidos do número lido.
numero = str(123)
print(f'O número {numero} invertido é: {numero[::-1]}')
print('-----')

# 47 - Leia um número de 4 dígitos (de a 1000 a 9999) e imprima 1 dígito por linha.
nm = 2234
nm = str(nm)
print(nm[0])
print(nm[1])
print(nm[2])
print(nm[3])
print('-----')

# 50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
idade = 25
ano_atual = 2022
print(f'Ano de nascimento do cidadão: {ano_atual-idade-1}')
print('-----')
