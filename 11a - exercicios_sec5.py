"""
                  ///Espaço reservado para solucionar alguns exercícios da seção 5///
"""

# 1
# x = input('Digite o primeiro número: ')
# y = input('Digite o segundo número: ')
# if x > y:
#     print(f'{x} é maior que {y}.')
# elif x < y:
#     print(f'{y} é maior que {x}.')
# else:
#     print(f'O número {x} é igual ao número {y}.')
# print('-----')


# 2
# x = float(input('Digite um número real: '))
# if x >= 0:
#     print(f'A raiz quadrada do número é: {x**0.5}')
# else:
#     print(f'O número não possui raiz real, já que {x} é negativo.')
# print('-----')

# 3
# x = float(input('Digite um número inteiro (Z): '))
# if x != int:
#     print(f"O número '{x}' será transformado em inteiro do tipo: {int(x)}")
#     if x % 2 == 0:  # Calculamos o resto da divisão com "%"
#         print(f'O número é par.\nA raiz quadrada: {(x**0.5)}')
#     else:
#         print(f'O número é impar.\nO número ao quadrado: {x**2}')
# else:
#     if x % 2 == 0:  # Calculamos o resto da divisão com "%"
#         print(f'O número é par.\nA raiz quadrada: {(x**0.5)}')
#     else:
#         print(f'O número é impar.\nO número ao quadrado: {x**2}')
# print('-----')

# 8
# nota1 = float(input('Insira a primeira nota: '))
# nota2 = float(input('Insira a segunda nota: '))
# if nota1 > 10 or nota1 < 0:
#     print(f'A nota {nota1} não é válida. Precisa estar entre 0 e 10.')
# elif nota2 > 10 or nota2 < 0:
#     print(f'A nota {nota1} não é válida. Precisa estar entre 0 e 10.')
# else:
#     print(f'A média aritmética: {(nota1+nota2)/2}')


# 11
# num = float(input('Insira um número inteiro maior que zero: '))
# if num != int and num > 0:
#     print(f"O número '{num}' será transformado em: {int(num)}")
# num = str(int(num))
# soma = []
# if int(num) > 0:
#     for i in num:
#         soma.append(int(i))
#     print(f'A soma dos algarismos: {sum(soma)}')
# else:
#     print(f"Número inválido.")


# 12 = Preciso refinar esse código
# numero = input('Digite um número inteiro: ')
# if int(numero) < 0:
#     print('O número é negativo.')
# else:
#     lista = list(range(0, int(numero)))
#     print(lista)
#     for i in lista:
#         if 10**i - int(numero) < 0.3:
#             print(f'O log de {numero} na base 10 é aproximadamente: {i}')


# 13 - Calcula a média ponderada
# notaProva1 = 6
# notaProva2 = 6
# notaProva3 = 6
# pesoProva1 = 1
# pesoProva2 = pesoProva1
# pesoProva3 = 2
# listaPeso = [pesoProva2, pesoProva3, pesoProva1]  # Não sei o que houve, mas não consegui usar o comando list aqui.
# mediaPonde = ((notaProva1*pesoProva1)+(notaProva2*pesoProva2)+(notaProva3*notaProva3))/sum(listaPeso)
# if mediaPonde >= 10:
#     print(f'VOCÊ ESTÁ APROVADO. Sua nota: {mediaPonde}')
# else:
#     print(f'VOCÊ ESTÁ REPROVADO. Sua nota: {mediaPonde}')

# Acho que ele está errando na suposta análise do cálculo da média ponderada
