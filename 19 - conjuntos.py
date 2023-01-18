"""
                    CONJUNTOS - BASEADO NO MESMO PRINCÍPIO DA TEORIA DOS CONJUNTOS DA MATEMÁTICA


Sets: no Python, os conjuntos são chamados de sets.
- Sets: não possuem valores ordenados
- Sets: não possuem valores duplicados (não gera erro, mas não duplica)
- Elementos não são acessados via índice. Ou seja, NÃO SÃO INDEXADOS
- São MUTÁVEIS, diferente das tuplas
- Os conjuntos são bons para:
    - Armazenar elementos, mas sem se importar com a ordenção, chaves, valores e itens duplicados
    - Referenciados com "{}". Lembrar que mapas também são representados por chaves. veja diferenças:

Diferenças entre conjuntos  (Set) e mapas (dicionários)
    - Dicionário: chave:valor
    - Conjunto: valor

Nota:
Podemos gerar sets para strings, listas, tupla, ...
Podemos obter muitas outras propriedades com o "dir" no console
"""

# Definindo um conjunto

# Forma 1: Menos comum

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Temos valores repetidos, que serão descartados na geração do set
print(s)
print((type(s)))
print('-----')

"""
Obs.: Ao criar um conjunto, caso seja adicionado um valor existente, o mesmo será ignorado sem gerar error e não fará 
parte do conjunto.
"""
print('-----')

# Forma 2: Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print((type(s)))
print('-----')

# Verificando se determinado elemento está no conjunto

n = 10
if n in s:
    print(f'Tem o {n} no conjunto')
else:
    print(f'Não tem o {n} no conjunto')
print('-----')

# Algumas diferenças importantes sobre nossas coleções:

# Listas aceitam valores duplicados e mantém a ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')
print('-----')

# Tuplas aceitam valores duplicados e mantém a ordem

tuupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tuupla} com {len(tuupla)} elementos')
print('-----')

# Dicionários não aceitam chaves duplicadas e MANTÉM a ordem

diicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'Valor')
print(f'Dicionário: {diicionario} com {len(diicionario)} elementos')
print('-----')

# Conjuntos não aceitam valores duplicados e geram uma ordem ALEATÓRIA

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjuntos: {conjunto} com {len(conjunto)} elementos')
print('-----')

# Podemos colocar diferentes tipos de dados no conjunto

ss = {1, 'b', True, 32.32, 44}
print(ss)
print(type(ss))
print('-----')

# Podemos iterar um conjuntos

# Formas interessantes de usar os conjuntos:

"""
Formulário de um museu.
Exemplo de aplicação:
Os visitantes visitam um museu anualmente. Adicionamos cada cidade de cada pessoa em uma lista Python, já que em uma 
lista podemos adicionar novos elementos de forma a ter repetição.
Aplicação abaixo:
"""
print('-----')

# No momento do cadastro

cidades = ['Belo Horizonte', 'Mato Grosso', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(f'Temos {len(cidades)} cadastros no museu')  # Agora sabemos quantos cadastros temos no museu
print('-----')

# Quantas cidades distintas temos? Vamos usar o set para analisar isso. Essa é uma sacada importante

print(f'temos {len(set(cidades))} cidades distintas')
print('-----')

# Adiconando elementos em um conjunto

# Forma 1: Usando o add()

sss = {1, 3, 4, 5}
print(sss)
print(type(sss))
print('-----')

sss.add(6)
sss.add(6)  # Duplicidade não gera erro
print(sss)
print(type(sss))
print('-----')

# Obs.: Não recomendo utilizar o update() nesse caso

"""
sss.update({55})  # Imprime com o valor 1
print(sss)  # Imprime sem o valor 1 - mas ainda não sei qual a explicação para isso
print(type(sss))
print('-----')
"""

# Removendo elementos de um conjunto. Não retornamos o valor que foi removido

# Forma 1: GERA UM ERRO ao remover um elemento que não existe no conjunto

sss.remove(6)  # Removemos o 6. Repare que não é via índice pelo fato de não ser indexado
print(sss)
print('-----')

# Forma 2: NÃO GERA UM ERRO ao remover um elemento que não existe no conjunto

sss.discard(1)  # Importante usar esse modelo
print(sss)
print('-----')

# Copiando um conjunto para outro

# Forma 1: Deep Copy. Ou seja, temos dois objetos independes

conj = {1, 3, 5, 7}
novo_conj = conj.copy()
print(novo_conj)
novo_conj.add(50)
print(conj)
print(novo_conj)
print('-----')

# Forma 1 - Shallow Copy. Aqui, quando mudamos em uma mudamos também na outra

outro_conju = conj
outro_conju.add(100)  # Aqui no Shallow Copy estamos adicionando tanto no outroConj quanto no conj
print(conj)
print(outro_conju)
print('-----')

# Podemos remover todos os elementos no conjunto

outro_conju.clear()
print(outro_conju)
print('-----')

# Métodos matemáticos dos conjuntos

"""
Imagine que temos dois conjuntos: 
- Estudantes do curso de Administração Pública
- Estudantes do curso de Engenharia de Petróleo
"""

estud_Adm = {'Ana', 'Carla', 'Frederico', 'Francisco', 'Endriw'}
estud_EP = {'Francisco', 'Endriw', 'Henrique', 'Amanda'}

"""
Obs.: Observe que temos repetição nos nomes. Ou seja, estão nos dois conjutnos. Precisamos gerar um conjunto com nomes 
de elementos únicos.
"""
print('-----')

# Forma 1: Utilizando union. Esse é recomendado, é mais explícito

unicos1 = estud_Adm.union(estud_EP)  # Aqui a ordem não importa
print(f'Estudantes únicos via union(): {unicos1}')

# Forma 2: Utilizando o caractere pipe "|"

unicos2 = estud_EP | estud_Adm  # Gera um conjunto de estudantes que estão em ambos os cursos
print(f'Estudantes únicos via pipe "|": {unicos2}')
print('-----')

# Forma 1: Utilizando intersection

ambos1 = estud_Adm.intersection(estud_EP)
print(f'Estudantes que estão em ambos os cursos via intersection(): {ambos1}')

# Forma 2: Utilizando "&"

ambos2 = estud_Adm & estud_EP
print(f'Estudantes que estão em ambos os cursos via &: {ambos2}')
print('-----')

# Agora, vamos gerar um conjunto de estudantes que não estão no outro curso. Ou seja, estão em um mas não em outro

apenas_EP = estud_EP.difference(estud_Adm)  # Exclui os estudantes de Administração Pública
print(f'Apenas em Engenharia de Petróleo {apenas_EP}')
apenas_Adm = estud_Adm.difference(estud_EP)  # Exclui os estudantes de Engenharia de Petróleo
print(f'Apenas em Administração Pública {apenas_Adm}')
print('-----')

# Soma, Valor máximo, Valor mínimo, Tamanho. Se os valores forem todos inteiros ou reais

s = {1, 3, 4, 5, 6, 7}
print(f'Soma dos valores do conjunto: {sum(s)}')
print(f'Valor máximo do conjunto: {max(s)}')
print(f'Valor mínimo do conjunto: {min(s)}')
print(f'Tamanho do conjunto: {len(s)}')
