"""
TUPLAS (tuple): BASTANTE PARECIDAS COM LISTAS, COM DUAS DIFERENÇAS BÁSICAS:

-Aceita diferentes tipos de dados.

- Tuplas são representadas por parênteses.
- Tuplas são IMUTÁVEIS, ou seja, ela nunca muda. Todas as operações em uma tupla gera uma nova tupla.
"""
# Nota 1: As tuplas são representadas por parênteses (). Mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
print('-----')

tupla2 = 1, 2, 3, 4, 5, 6,  # Também cria uma tupla. Posso ou não usar a vírgula no final.
print(tupla2)
print(type(tupla2))
print('-----')


# Nota 3: Tuplas com 1 elemento, não é uma tupla, é um inteiro.
tupla3 = (1)
print(tupla3)
print(f'Veja que é do tipo inteiro: {type(tupla3)}')
print('-----')

# Nota 4: Isso é uma tupla. Criamos com a vírgula.
tupla4 = (1,)
print(tupla4)
print(type(tupla4))
print('-----')

tupla5 = 25,
print(tupla5)
print(type(tupla5))
print('-----')


"""
Em conclusão: tuplas são definidas pela uso das vírgulas, e não pelo parênteses. Isso é importante.
"""

# Também podemos gerar tuplas com o range.
tupla6 = tuple(range(20, -22, -2))
print(tupla6)
print(type(tupla6))
print('-----')

# Desempacotamento de tuplas. Funciona da mesma forma que as listas.
tupla = ('Francisco', 'Araújo', 'da', 'Silva')
nome, sobre_nome, terceiro_nome, quarto_nome = tupla
print(nome)
print(sobre_nome)
print(terceiro_nome)
print(quarto_nome)
print('-----')

"""
Métodos para adição e remoção de elementos nas tuplas não existem, já que são imutáveis.
"""

# Se os valores forem inteiros ou reais: soma*, valor máximo*, valor mínimo*, tamanho*
tupla7 = 1, 1, 5, 6, 5, 4, 9, 8.1
print(f'soma: {sum(tupla7)}')
print(f'máximo: {max(tupla7)}')
print(f'mínimo: {min(tupla7)}')
print(f'tamanho: {len(tupla7)}')
print('-----')

# Concatenação de tuplas
tupla8 = 1, 2, 3,
print(tupla8)

tupla9 = 2, 5, 1
print(tupla9)

tupla10 = (tupla8 + tupla9)
print(tupla10)
print(type(tupla10))
print(tupla8)
print(tupla9)
print('-----')

# Tuplas são imutáveis, mas posso sobrescrever uma tupla. Informação importante.
tupla8 = tupla8 + tupla9
print(f'Tupla 8 sobrescrita: {tupla8}')
print('-----')

# Podemos verificar se determinado elemento está em uma tupla.
tupla11 = 2, 6, 4, 1, 2, 3, 6, 9,
print(1 in tupla11)  # Maneira interessante de fazer essa verificação
print(15 in tupla11)
print('-----')

# Iterando em uma tupla.
for n in tupla11:
    print(n)
print('-----')

# Gerando índice para os elementos na tupla.
for indice, valor in enumerate(tupla11):
    print(f'índice: {indice}', f'valor: {valor}')  # Gostei dessa opção
print('-----')

# Contando elementos dentro de uma tupla.
tupla12 = ('a', 'b', 'a', 'c', 'd', 'f', 'g', 'l', 'a', 'k', 'j', 'e', 'a', 'i', 'b')
elemento = 'b'
print(f"Possui '{tupla12.count(elemento)}' elementos '{elemento}' na tupla em estudo!")
print('-----')

# Posso transformar uma string em uma tupla.
umaString = 'Francisco Araújo'
print(umaString)
print(type(umaString))
print('-----')

umatupla = tuple(umaString)
print(umatupla)
print(type(umatupla))
print('-----')

"""
Exemplos para o bom uso de tuplas.
"""

# Exemplo 1: meses, já que nunca mudam
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses)
print('-----')

# Como acessar o elemento de uma tupla?
print(meses[3])  # ou seja, é indexado
print('-----')

# iterando sobre uma tupla.
indice = 0
while indice < len(meses):
    print(meses[indice])
    indice += 1
print('-----')

# qual o índice do elemento?
print(meses.index('fev'))
print('-----')

# slicing: tupla[inicio:fim:passo], ou seja, mesmo usando tuplas, temos que usar colchetes para o slicing.
print(meses[5:8])

"""
- Porque utilizar tuplas? são mais rápidas do que listas. Ótimo para big data, AI. Ganhamos performance.
- Tuplas deixam seu código mais seguro, já que os elementos imutáveis trazem segurança para o código
"""
print('-----')

# Copiando uma tupla para outra.
tupla = (1, 2, 3)
print(f'Primeira tupla: {tupla}')

nova = tupla

print(f'Nova tupla: {nova}')
print(f'Primeira tupla: {tupla}')

outra = (3, 4, 0)

nova = nova + outra  # Na tupla não temos o diferencial da Shallow Copy. Ous seja, não tem vínculos aqui na tupla.

print(f'nova + outra: {nova}')
print(tupla)
