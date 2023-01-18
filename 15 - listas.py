"""
                                            LISTAS - SÃO MUTÁVEIS


Listas: Em Python funciona como vetores/matrizes (arrays). Aqui, nossas listas são DINÂMICAS e podemos inserir QUALQUER
TIPO de dado nela.

No Python:
    - Dinâmico: não possuem tamanho fixo, ou seja, podemos criar e incrementar elementos, mas o tamanho não é infinito,
    depende do tamanho da memória da máquina que você está usando
    - Qualquer tipo de dado: não possuem tipo de dado fixo
    - Listas em Python são represetadas entre colchetes []
    - O python é uma das linguagens mais usadas no campo da biotecnologia

 Faça (no terminal): type([]): você será informado que o tipo é uma lista.

 Obs.: Faça dir(lista) no termina. Essa ação nos mostrará todos os métodos para essa variável do tipo lista (você vai
 criar essa lista e depois aplicar a ação).
"""

# from typing import List

print(type([]))
print('-----')

lista1 = [1, 2, 5, 6, 1, 4, 6, 12, 45]  # Lista de números inteiros
lista2 = ['F', 'r', 'a', 'n', 'c', 'i', 's', 'c', 'o']  # Lista de strings
lista3 = []  # Lista vazia
lista4 = list(range(11))  # Transforma os dados de zero a dez do range em uma lista
lista5 = list('Francisco Araújo')  # Gera uma lista com um único elemento do tipo string
print('-----')

# Podemos, facilmente, checar se um elemento esta na lista com a função "in"

n = 11
if n in lista1:
    print(f'Encontrei o valor {n} na lista!')
elif n-1 in lista1:
    print(f'O valor {n} não está na lista, mas econtramos o valor {n-1}, que é n - 1!')
elif n+1 in lista1:
    print(f'O valor {n} não está na lista, mas encontramos o valor {n+1}, que é n + 1!')
else:
    print(f"Valor '{n}' não foi encontrado na lista!")
print('-----')

# Podemos facilmente ordenar uma lista, de strings ou numérica. Não importa se houver elementos repetidos

lista1.sort()  # Uma vez ordenado, a lista anterior não existe mais, apenas a ordenada
print(lista1)
print('-----')

# Podemos contar o número de ocorrências de um valor em uma lista

print(f'Ocorrência no número "1" na lista 1: {lista1.count(1)}')
print(f"Ocorrência da letra 'a' na lista 5: {lista5.count('a')}")
print('-----')

"""
Podemos adicionar elementos em uma lista: Utilizando a função "append", inclusive valor repetido. Todavia, conseguimos
incrementar apenas um ELEMENTO (importante notar que uma lista também é um elemento) por vez.
"""

print(f'Lista 1: {lista1}')
lista1.append(1)
print('Adicionamos o número 1 na lista1:')  # Essa adição de elemento é feita no final da lista
print(lista1)
print('Usamos [] para incrementar uma lista dentro de outra lista.')
lista1.append([1, 2, 3, 4, 5, 6, 7])
print(lista1)
print('-----')

# Mas atenção! Cuidado ao procurar dados nessa lista, já que ela possui mais de um tipo de elemento

if [1, 2, 3, 4, 5, 6, 7] in lista1:
    print('Ótimo, encontrei a lista incrementada (o elemento lista na verdade)!')
else:
    print('Não encontrei o elemento lista! Verifique novamente!')
print('-----')

# Como encontrar um elemento que está na lista incrementada?

n = 3
if n in lista1[len(lista1) - 1]:  # Acessando a última posição da lista, que é a lista que contém nosso elemento
    print(f'Encontrei o elemento "{n}" na lista 1 incrementada!')
else:
    print(f'Não encontrei o elemento "{n}" na lista 1 incrementada!')
print('-----')

"""
Raciocínio para o if acima:
A função len conta quantos elementos temos na lista, ou seja, 11 elementos. No entanto, como o Python possui posição
0, nossa lista incrementada está na posição 10, por isso acessamos ela na posição [len(lista1) - 1] = 10
"""

"""
Outra forma de adicionar elementos na lista, mas são adicionados individualmente. Ou seja, a lista continuará com 1 
elemento.
Outro detalhe importante é que essa função não aceita valor único. Para isso temos que usar o append().
"""

lista1.extend([1, 2, 3, 4, 5, 6, 7])
print(lista1)
print('-----')

# Podemos inserir (e não substituir) um elemento na lista especificando a posição do elemento na lista

print(f'Lista 1: {lista1}')
lista1.insert(2, 'Elemento adicionado na terceira posição com a função insert')
print(lista1)
print('-----')

# Podemos também juntar duas listas

lista6 = lista1 + lista2  # Faz o mesmo trabalho do extend
print(lista6)
print('-----')

# Podemos inverter uma lista

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
print('-----')

# Outro jeito de inverter

print(lista5[::-1])
print('-----')

# Podemos copiar uma lista

lista7 = lista6.copy()
print(lista7)
print('-----')

# Podemos saber quantos elementos temos na

print(f'A lista7 tem {len(lista7)} elementos')
print('-----')

# Podemos excluir o último elemento da lista. O pop remove e retorna o último elemento. Verifique no terminal

print(lista5)
lista5.pop()
print(lista5)
print('-----')

"""
Podemos também remover pelo índice. Os elementos a direita do índice são deslocados para a esquerda. Com isso, novos
índices são criados. Esse detalhe é muito importante.
"""

print(lista5)
lista5.pop(1)
print(lista5)
print('-----')

# Podemos remover todos os elementos

print(lista5)
lista5.clear()
print(lista5)
print('-----')

# Repetindo uma lista

nova = [1, 2, 4, 6, 8, 0]
nova = nova * 3
print(nova)
print('-----')

# Posso transformar um texto (string) numa lista a cada espaço (se não especificado no argumento do split) da expressão

nova = 'Francisco Araújo da Silva'
print(nova.split())
print('-----')

# Para separar a cada vírgula
nova = 'Francisco,Araújo,da,Silva'
print(nova.split(','))
print('-----')

# Concatenando elementos de uma lista por espaço e transformando em uma string. Será que vale apenas para string?

umTexto = ['Francisco', 'Araújo', 'da', 'Silva']
umaString = ' '.join(umTexto)
print(umaString)
print('-----')

# Numa lista, realmente, podemos colocar qualquer tipo de dado

listaVariada = [1, 2.32, True, 'Francisco', 'd', [1, 2, 3], 45462656]
print(listaVariada)
print('-----')

# Exemplo 1 com o for. Agora, vamos iterar em uma lista. Ou seja, vamos imprimir cada elemento

for elemento in listaVariada:
    print(elemento)
print('-----')

"""
# Exemplo 2 - usando o while.
carrinho = []  # Criamos uma lista vazia
produto = ''  # Variável do tipo string, para adicionar ao carrinho

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair e exibir o carrinho de produtos: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(f'Todos os produtos adicionados ao carrinho são: {produto}')
"""
print('-----')

# Podemos também criar uma lista com variáveis. Isso pode ser muito interessante

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numerosV = [num1, num2, num3, num4, num5]
print(numerosV)
print('-----')

# Nas listas, fazemos acesso aos elementos de forma indexada (via índice)

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco
print('-----')

"""
Podemos, também, acessar de trás para frente. Pense nas listas como um círculo, pode ajudar a acessar os elementos nessa
ordem.
"""

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
print('-----')

# Loop nas cores com for

for cor in cores:
    print(f'As cores com o loop for: {cor}')
print('-----')

# Loop nas cores com o while

indice = 0
while indice < len(cores):
    print(f'As cores com o loop while: {cores[indice]}')
    indice = indice + 1  # == indice += 1
print('-----')

cores = ['verde', 'amarelo', 'azul', 'branco']

# Podemos gerar índices em uma lista

for indiceDaLista, cor in enumerate(cores):
    print(f"índice da lista: {indiceDaLista}, Cor no índice:  {cor}")
# Ou seja, o  enumerate gera pares, chave e valor para a lista. A chave vair para "indiceDaLista" e valor para "Cor"

"""
Faça no terminal: cores = ['cor1', 'cor2', 'cor3', 'cor4', 'cor5', 'cor6', 'cor7']
list(enumerate(cores))
"""
print('-----')

# Lista aceita valores repetidos (reforçando)

lista = list([])

"""
Com o append() abaixo vamos adicionar elementos nessa lista vazia.
Essa declaração de lista, para criar lista vazia, é o jeito correto de criar sem gerar a cobrinha em baixo dele.
"""

lista.append(3)
lista.append(2)
lista.append(5)
lista.append(0)
lista.append(8)
lista.append(8)
lista.append(7)
print(lista)
print('-----')

"""
Agora vamos aprender outros métodos, mas não tão importantes, para continuar trabalhando com listas.
"""

# Encontrar o índice de um elemento em uma lista. Se o elemento não estiver na lista, UM ERRO É GERADO

lista10 = [1, 3, 5, 6, 3, 8, 9, 5, 4, 7]
print(f'O índice: {lista10.index(5)}')
print(f'O índice: {lista10.index(6)}')
print(f'O índice: {lista10.index(3)}')  # Gera o índice da primeira ocorrência, por isso, atenção se existir repetição
print('-----')

# Podemos fazer buscas dentro de um range, indicando qual o índice do ínicio da busca

print(lista10.index(3, 2))
# Procura o valor 3, a partir do índice 2. Ou seja, dentro de um range, busca o índice de acordo com a lista original
print('-----')

# Podemos fazer buscas dentro de um range. Valor, início, fim

print(lista10.index(6, 2, 7))
print('-----')

# Revisando o slicing

# lista[início:fim:passo]. Parece com o range(início:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'início'

lista = [1, 2, 3, 4, 5]
print(lista[1:])  # Imprime a lista a  partir do índice 1, ou seja, a partir do 2. Também aceita valores negativos
print('-----')

# Trabalhando com o parâmetro fim

print(lista[:2])  # Imprime do início até o índice 2
print('-----')

# Trabalhando com início e fim

print(lista[1:3])  # Imprime do índice 1 até o índice 2
print('-----')

# Trabalhando com o passo. Podemos usar valor negativo para o passo

print(lista[1::2])  # Imprime de 1 até o final de 2 em 2
print('-----')

# Trocando os valores em uma lista de lugar

nome = ['Francisco', 'Araújo', 'da', 'Silva']
nome[0], nome[1], nome[2], nome[3] = nome[2], nome[1], nome[3], nome[0]  # Forma diferente de atribuição
print(nome)
print('-----')

# Modo Pythônico alinhado. Inverte a lista

nome = ['Francisco', 'Araújo', 'da', 'Silva']
nome.reverse()
print(nome)
print('-----')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho*
# Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # valor máximo
print(min(lista))  # valor mínimo
print(len(lista))  # tamanho da lista
print('-----')

# Podemos transformar uma lista (colchetes) em uma tupla (parênteses) - estudaremos mais adiante

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

"""
VISUALMENTE A ÚNICA DIFERENÇA SÃO OS COLCHETES E OS PARÊNTES. Mas tem mais coisas por trás de tudo isso. Em breve 
estudaremos afinco.
"""
print('-----')

# Fazendo o desempacotamento da lista. É importante notar que o número de variáveis deve ser igual ao len da lista
lista = [1, 2, 3, 4, 5, 6]
nu1, nu2, nu3, nu4, nu5, nu6 = lista
print(nu1)
print(nu2)
print(nu3)
print(nu4)
print(nu5)
print(nu6)
print('-----')

"""
Muito cobrado em entrevista. Copiando uma lista para outra (Shallow Copy e Deep Copy).
"""

# Deep Copy

lista = [1, 2, 3]
print(f'lista criada {lista}')

novalista = lista.copy()
print(f'Lista copiada {novalista}')

novalista.append(4)

print(f'Lista criada: {lista}')
print(f'Lista copiado com o copy() adicionando elemento com o append(): {novalista} ')

"""
Veja que são duas listas diferentes. Ou seja, é o Deep Copy.
lista.copy >> copia uma lista, mas sem vínculo. Em python é chamado de Deep Copy
"""
print('-----')

# Shallow Copy

lista = [1, 2, 3]
print(f'lista criada {lista}')

nova = lista  # Uma forma de cópia, que também é uma atribuição
print(f'lista copiada com vínculo {nova}')

nova.append(4)

print(f'lista criada {lista}')
print(f'lista copiada {nova}')

"""
Utilizamos a cópia via atribuição. Copiamos o dado da lista para uma nova lista. Todavia, ao modificar uma, modificamos 
a outra. Em Python é chamado de Shallow Copy.Isso é muito importante.
"""
