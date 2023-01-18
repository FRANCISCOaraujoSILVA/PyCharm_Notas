"""
                                                    DICIONÁRIOS


- Em algumas linguagens de programação, os dicionários Python são conhecidos por MAPAS
- Dicionários são coleções do tipo chave/valor. Ou seja, mapeamento entre chave-valor
- Dicionários são representados por {}, faça: print(type({}))
- O conjunto chave-valor pode ser de qualquer tipo (podemos misturar dados), e seprados por ':'
Ex.: chave:valor
"""

# Criação de dicionários

# Forma 1: A mais comum. O conjunto chave-valor é um elemento, portanto, temos três elementos. Recomendado

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# print(paises)
# print(type(paises))

# Forma 2: Menos comun, mas acho essa melhor. Observe que o dicionário é criada pela palavra reservada, e não pelo "{}"

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
print('-----')

# Acessando elementos. Lembrar que eles NÃO são indexados

# Forma 1: Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])  # Gera um erro se a chave não existir, keyerror, tratar o erro é mais complicado
print('-----')

# Forma 2: Acessando via get - RECOMENDADO, pois não gera erro, gera None se a chave não existir

print(paises.get('br'))
print(paises.get('ru'))  # Gera um aviso tipo None (não um erro), se o valor não for encontrado
print('-----')

# Imagine a aplicação abaixo. Veja a vantagem de usar o None a partir da forma 2

novosPaises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
pais = novosPaises.get('pa', 'PAÍS NÃO ENCONTRADO!')

"""
Olha aí, é mais vantajoso usar o elemento get. Assim, nem precisaríamos mais do if e do else. Posso deixar um recado se 
não encontrar o valor. Esse detalhe é muito importante.
"""

print(f'Encontrei o país {pais}!')
print('-----')

"""
if russia:
    print(f'Encontre o país {novosPaises}!')
else:
    print('Não encontrei o país!')
"""
print('-----')

# Podemos verificar se uma CHAVE está dentro do dicionário

print('br' in novosPaises)  # Está no dicionário, True
print('ru' in novosPaises)  # Não está no dicionário, False
print('Estados Unidos' in novosPaises)  # 'Estados Unidos' está no dicionário, mas não é chave, False
print('-----')

"""
Podemos utilizar qualquer tipo de dado (int, float, string, booleano), incluisive lista, tupla dicionário, como 
sendo as chaves dos dicionários.
"""

# Ex.: Localidades com as respectivas coordenadas geográficas (fictícias)

localidades = {
    (35.6565, 6365.656): 'Escritório em Tókio',
    (40.6652, 4569.632): 'Escritório em Singapura',
    (63.3215, 7849.5623): 'Escritório em Londres',
}

print(localidades)
print(type(localidades))

"""
Veja, em localidades, usamos tuplas como chaves para o nosso dicionário. A tupla é uma boa tática para usar como chave
de dicionário, já que ela é imutável.
"""
print('-----')

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))
print('-----')

# Forma 1: Mais comum e mais fácil

receita['abr'] = 350  # muito simples
print(receita)

# Forma 2: Boa também

novo_dado = {'mai': 500}
receita.update(novo_dado)  # Achei essa forma 2 muito top. receita.update({'mai': 500}) - é a mesma coisa
print(receita)
print('-----')

# Atualizando/modificando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)
print('-----')

"""
CONCLUSÃO1: A forma de adicionar elementos em um dicionário ou atualizar dados em um dicionário é a mesma.
CONCLUSÃO2: Em dicionários, NÃO podemos ter chaves repetidas. Já que se isso ocorrer, estamos, na verdade, atualizando.
"""

# Removendo dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1: Mais comum (retorna o valor removido), preciso indicar o índice se não for o último elemento

ret = receita.pop('mar')  # O pop remove o último (na forma padrão) elemento da lista. Aqui, precisamos indicar a chave
print(f'O VALOR retirado com o pop é sempre mostrado: {ret}')
print(receita)
print('-----')

# Forma 2: Mais interessante, mas não retorna o valor removido. A vantagem é que não preciso indicar o índice da chave

del receita['jan']
print(receita)
print('-----')

# Porque usar dicionários?

# Imagine que você tem um comércio eletrônico, onde temos carrinhos de compras para adicionar produtos

"""
Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# Poderíamos usar uma lista para isso? Sim! Mas não saberíamos quais são os índices (descrição do elemento)

Carrinho = []
Produto1 = ['Xadrez', 1, 230.00]
Produto2 = ['Pincel', 1, 150.00]

Carrinho.append(Produto1)
Carrinho.append(Produto2)
print(Carrinho)  # Na verdade, é uma lista de lista. Temos 2 produtos. Cada produto tem 3 índices
# Teríamos que saber qual é o índice de cada informação no produto
print('-----')

# Poderíamos utilzar uma tupla para isso? Sim

Produto1 = ('Xadrez', 1, 230.00)
Produto2 = ('Pincel', 1, 150.00)

carrinho = (Produto1, Produto2)
print(carrinho)  # Também, teríamos que saber qual o índice de cada elemento nos 2 produtos
print('-----')

# Poderíamos utilizar um dicinário para isso? Sim, e com vantagem, pois temos a descrição do índice

carrinho = []
produto1 = {'Nome': 'Xadrez', 'Quantidade': 1, 'preço': 230.00}
produto2 = {'Nome': 'Pincel', 'Quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)  # Temos os índices bem explícitos, rico em detalhes. Fica melhor para visualizar. Evita problemas

"""
Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre
cada informação.
Cada coleção possue suas particularidades, mas elas se completam.
"""
print('-----')

# Métodos de dicionários

# No terminal, faça: dir({}) e veja os vários métodos

d = dict(a=1, b=3, c=4)
print(d)
print(type(d))

# Limpando o dicionário

"""
d.clear()
print(d)
"""

# Copiando um dicionário

novo = d.copy()  # Deep Copy
print(novo)
novo['d'] = 10

print(d)
print(novo)
print('-----')

# Forma 2: Shallow Copy - com vínculo

novo = d
print(novo)
novo['d'] = 10
print(d)
print(novo)
print('-----')

"""
Forma não usual de criação de dicionários:
outro = {}.fromkeys('chave', 'valor')  # Assim, para cada letra de 'chave' é uma chave para 'valor'. Mas não repete.
"""

outro = {}.fromkeys('A', 'B')  # Sempre teremos o mesmo valor para chaves diferentes
print(outro)
print(type(outro))
print('-----')

# Criando várias chaves

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

"""
O método fromkeys recebe dois parâmetros: um interável e um valor.
Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
"""
print('-----')

# Outra dica
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
