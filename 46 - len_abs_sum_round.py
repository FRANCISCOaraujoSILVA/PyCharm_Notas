"""
                                          LEN, ABS, SUM E ROUND


- Len(): Retorna o tamanho
- Abs(): Retorna o valor absoluto de um número inteiro ou real
- Sum(): Recebe como parâmetro um iterável e retorna a soma total dos elementos + um valor inicial (default=0)
- Round(): Retorna um número arredondado para n digítos de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo
"""

lista = [1, 2, 3, 4, 5]

# Tamanho

print(len(lista))
print('-----')

# Valor absoluto

print(abs(-3))
print('-----')

# Soma
print(sum(lista))
print(sum(lista, 5))  # Observe que a soma da lista é 15. 15 + 5 = 20
print(sum((3.15, 3.17)))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))  # Estamos dizendo que queremos somar os valores
print('-----')

# Arredondar

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2112121212121, 2))  # Arredonda para duas casas decimais após a vírgula
