"""
Len, Abs, Sum e Round

len(): retorna o tamanho
abs(): retorna o valor absoluto de um número inteiro ou real
sum(): recebe como parâmetro um iterável e retorna a soma total dos elementos + um valor inicial (default=0)
round(): retorna um número arredondado para n digítos de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada
"""
lista = [1, 2, 3, 4, 5]


# tamanho
print(len(lista))
print('-----')

# Valor absoluto
print(abs(-3))
print('-----')

# soma
print(sum(lista))
print(sum(lista, 5))
print(' ')
print(sum((3.15, 3.17)))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))  # Estamos dizendo que queremos somar os valores
print('-----')

# arredondar

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2112121212121, 2))  # arredonda para duas casas decimais após a vírgula




