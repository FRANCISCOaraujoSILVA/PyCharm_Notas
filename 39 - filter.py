"""
                                                        FILTER


- Filter(): utizado para filtrar dados de uma determinada coleção
- Usado para remoção de dados faltantes: fundamental para quem quer trabalhar com ciência de dados, para não distorcer
o resultado final
- A função filter() recebe dois parâmetros, uma função e um iterável assim como o map()
- Assim como o Map, aqui, usamos os dados apenas uma veza
- Lambda + filter parece uma ótima combinação
- O objetivo é conhecer o Python e pensar fora da caixa
- Uma vez aplicado Map() e Filter(), fica claro que você conhece o Python
- Retornamos um objeto


Diferença clara entre Map() e Filter():
    Map; Rertona valores. Recebe uma função e um iterável e retorna um objeto mapeando a função para cada elemento
do iterável
    Filter; Retorna True ou False (booleano) para ser usado como filtro. Recebe uma função e um iterável e retorna
um objeto filtrando apenas um elemento de acordo com a função
"""

# Biblioteca para trabalhar com estatística
import statistics

valores = 1, 2, 3, 4, 5, 6, 7, 8, 9,
print(type(valores))
media = (sum(valores))/len(valores)
print(f'A média: {media}')
print('-----')

# Dados coletados de algum sensor

dados = [1.3, 3.7, 0.8, 4.1, 4.3, -0.1]

# Função mean() da biblioteca statistics

med = statistics.mean(dados)  # Muito melhor
print(f'A média: {med}')
res = filter(lambda x: x > med, dados)  # O 'x' representa cada dado da função. Retorna os dados maiores que a média
# Nessa análise do filter, retornamos True ou False
print(type(res))
print(list(res))
print('-----')
print(f'Não imprime novamente: {list(res)}')
print('-----')

# Dados faltantes

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(f'Sem o filter:\n {paises}')
print(f'Com o filter:\n {list(filter(None, paises))}')

"""
O None vai remover os espaços em branco e usar
os não vazios. Recomendado.
"""

print(f'Com lambda:\n {list(filter(lambda pais: len(pais) > 0, paises))}')  # u pais != ''
print('-----')


# Exemplo mais complexo. Temos uma lista cujos elementos são dicionários

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo gatos"]},
    {"username": "Larissa", "tweets": []},
    {"username": "Pedro", "tweets": []},
    {"username": "Eliza", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Anna", "tweets": []}
]


print(f'Os usuários do twitter:\n {usuarios}')
print('-----')

# Filtrar os usuários inativos no twitter. Aqueles sem tweets

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

"""
Ou seja, para cada elemento de "usuários" passamos para a variável "u", e fazemos a seleção com as propriedades dos
dicionários
"""

print(f'Usuários inativos no twitter:\n {inativos}')
print('-----')
print(f"Usuários ativos no twitter:\n {list(filter(lambda u: len(u['tweets']) != 0, usuarios))}")

# Refatorando os usuários inativos

"""
No terminal: 
usuarios = {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]}
usuarios
not usuarios['tweets'] -> gera False, já que possui tweets. Se possui tweets gera True, mas not gera a negação.
Portanto, o vazio significa False e não vazio significa True
"""

# Modo avançado

inativos2 = list(filter(lambda usuario: not usuario['tweets'], usuarios))  # Modo avançado

"""
Ou seja, uma lista vazia transformada em booleano gera False: usuario['tweets']
"""

print(f'Os novos inativos refatorados:\n {inativos2}')
print('-----')


# Combinando map() e filter()

"""
Tarefa: criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos que 5 caracteres.
"""

nomes = ['Carla', 'Roberto', 'Larissa', 'Letícia', 'Bia', 'Lois']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))  # Top

"""
Observe que filter() está dentro de map() como segundo argumento já filtrado, já que o map() recebe dois parâmentros
"""

print(f'A classificação das instrutores:\n {lista}')
