"""
-É importante prestar atenção às saídas de erros
-clicar no endereço "File"; vai nos redirecionar para o erro


Erros mais comuns em Python:

- SyntaxError: quando o Python encontra erro de sintaxe
def funcao:
    print('Francisco Araújo')

- NameError: quando uma variável ou função não foi definida
a) print(Francisco)
b) Nunca vair entrar no loop, msg não existe nessas condições. Vai gerar NameError
a = 19
# a = 'Qualquer coisa' # é uma maneira de contornar esse erro
if a < 10:
    msg = 'É menor que 10'

print(msg)

- TypeError: quando uma função/operação/ação é aplicada a um tipo errado
a) print(len(5))  # Essa funçõa só pode ser aplicado a um iterável
b) print('Franciso' + [])  # não conseguimos concatenar uma string com uma lista vazia

- IndexError: quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice
inválido. Quando um elemento é indexado? quando podemos fazer acesso a algum elemento via índice.
a) só temos o índice 0 nessa lista
lista = ['Eu']
print(lista[1])

b) Não temos a posição 2 dentro da string
lista = ['Eu']
print(lista[1][2])

-ValueError: Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo correto mas valor
inapropriado
a) Não conseguimos converter essa string para o número 1
print(int('um'))

- KeyError: quando tentamos acessar um dicionário com uma chave que não existe
a) não possui a chave
dic = {}
print(dic['Chave'])

- AttributeError: quando uma variável não tem um atributo ou função
a) A função sort() nõa é atributo para tuplas, mas sim para listas
tupla = (1, 3, 2, 0)
tupla.sort()
print(tupla)

- IndentationError: quando nõo respeitamos a indentação do Python (4 espaços)
Um dos primeiros erros que os programadores encontram no início
a) Falta espaço para indentar
def nova():
print('Francisco')

Obs.: Exceptions e Erros são sonônimos na programção. "Deu exception no código"
Obs.: É importante verificar as saídas de erros
"""





