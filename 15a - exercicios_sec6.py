"""
                  ///Espaço reservado para solucionar alguns exercícios da seção 6///
"""

# 1: Múltiplos de 3
# lista = list(range(0, 500, 3))
# print(lista[0:5])
# print('-----')

# 2.1: Usando o for
# limite = 100
# for i in range(0, limite+1):
#     print(i)
#     if i == limite:
#         for h in range(0, limite+1):
#             print(h)
#             if h == limite:
#                 for m in range(0, limite+1):
#                     print(m)
# print('------')

# 2.2: Usando while
# limite = 0
# parada = 0
# while limite < 101:
#     limite += 1
#     print(limite)
#     if limite == 100:
#         limite = 0
#         parada += 1
#     print(limite)
#     if parada == 3:
#         break
# print('-----')

# 3: Contagem regressiva
# cont = 0
# while cont < 10:
#     cont += 1
#     print(cont)
# print('FIM')
# print('-----')

# 4: Com passos
# limite = int(input('Digite um valor inteiro maior que 10_000: '))
# olimite = 0
# while olimite < limite:  # Uma forma diferente de representar o valor 10000. É melhor para visualizar
#     olimite += 1_000
#     print(olimite)
# print('-----')


# 5
# n = 0
# lista = []
# while True:
#     n += 1
#     x = float(input('Digite o primeiro valor para somar no final: '))
#     lista.append(x)
#     if n == 10:
#         break
# print(' ')
# print(f'A soma dos valores: {sum(lista)}')
# print('-----')

# 7
# lista = [1, 10, -1, -2, 5, 6, 4, 3, 2, 5]
# positivos = []
# for i in lista:
#     if i > 0:
#         positivos.append(i)
# print(f'A média aritmética dos valores positivos: {sum(positivos)/len(positivos)}')
# print('-----')

# 8
# print(f'O menor valor lido da lista: {min(lista)}')
# print(f'O maior valor lido da lista: {max(lista)}')
# print('-----')

# 10: Somar os pares e positivos
# lista = [1, 10, -1, -2, 5, 6, 4, 3, 2, 5]
# lista_pares = []
# for i in lista:
#     if i > 0:
#         if i % 2 == 0:
#             lista_pares.append(i)
# print(f'A soma de todos os pares da lista: {sum(lista_pares)}')
# print('-----')


# 17
# inteiro = int(input("Digite um número inteiro para criar uma lista de 0 até ele: "))
# quantidades = int(input("Escolha o índice até onde devemos somar os elementos na lista: "))
# listint = list(range(0, inteiro))
# print(f'A soma dos números até o índice da lista: {sum(listint[0:quantidades])}')
# print(listint)
# print('-----')

# 18 - Não era o que o  exercício pedia, mas gostei depois de feito e resolvi não apagar. Tudo pela arte do código
# numeros = list(range(0, int(input("Insira um valor como índice para que uma lista seja criada de 0 até ele: "))))
# parada = int(input('Escolha até qual índice devemos contar: '))
# contagem = []
# print(numeros)
# print(f"O maior deles: {max(numeros)}")
# for i in numeros:
#     contagem.append(i)
#     if i == parada:
#         break
# print(f"Foram feitas '{len(contagem)}' leituras.")
# print('-----')

# 24
# divisores = []
# inteiro = int(input('Digite um número inteiro:  '))
# lista = list(range(1, inteiro))
# lista_divisores = []

# for i in lista:
#     if inteiro % i == 0:
#         lista_divisores.append(i)

# print(f'A soma dos divisores: {sum(lista_divisores)}')
# print(f'A lista dos divisores: {lista_divisores}')
# print('-----')

# 25
# lista = list(range(0, 1001))
# multiplos = []
# for i in lista:
#     if i % 3 == 0:
#         multiplos.append(i)
#     else:
#         if i % 5 == 0:
#             multiplos.append(i)

# print(f"A soma de todos os multiplos: {sum(multiplos)}")
# print(f"A lista de todos os multiplos: {multiplos}")
print('-----')

# 26
# numero = int(input('Digite um número: '))
# multiplos = [11, 13, 17]
# lista_multiplos = []
# for i in multiplos:
#     if numero % i == 0:
#         lista_multiplos.append(i)

# if len(lista_multiplos) > 0:
#     print(f'Os múltiplos: {lista_multiplos}')
# else:
#     if len(lista_multiplos) == 0:
#         print(f'Esse número não possui os seguintes múltiplos: {multiplos}')

# if len(lista_multiplos) > 0:
#     for i in lista_multiplos:
#         if numero > i:
#             print(f'O múltiplo mais próximo: {i}')
#         if numero < i:
#             print(f'O múltiplo mais próximo: {i}')
