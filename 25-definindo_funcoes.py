"""
DEFININDDO FUNÇÕES:

- pode ou não receber entrada de dados e retornar uma saída de dados.
- muito usado para processos repetitivos.

OBS.:  Se a função criada realiza muitas tarefas, é bom fazer uma verificação para que a função seja simplificada.
Faça print(help(print())) para ver uma ducumentação ou ctrl+click no nome da função
"""
# exemplo de utilização de funções nativas (built-in):

cores = ['verde', 'amarela', 'azul', 'branco']
curso = ['Engenharia']

cores.append('roxo')  # adicionamos a cor "roxo" ao final da LISTA
curso.append('Administração Pública')
print('-----')

# utilizando a função integrada (Built-in) do Python print()

print(cores)
print(curso)
print('-----')

# cores.clear()  limpa a lista. Essa função não recebe dados de entrada
# print(cores)
print('-----')

# DRY - Don't Repeat Yourself (não repita você mesmo). Expressão muito usada na programação.

"""
Em python, a forma geral para definir função é:
def: definition

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
obs.:
nome_da_funcao: Sempre com letras minúsculas e separar com underline quando preciso.
parametros_de_entrada: São opcionais, se houver mais de um, separar por vírgula.
bloco_da_funcao: Também chamado de corpo da função, pode ou não ter o retorno da função.

Abrimos o bloco de código com o dois pontos ":"
Palavra reservada: def
"""
# Definindo a primeira função


def diz_oi():
    print('Olá usuário!')


"""
- Essa função "diz_oi" não recebe parâmetro de entrada.
- Essa função não retorna nada, pois fizemos apenas a definição dela.
- Podemos usar função dentro de outra função. Veja o "print", que está dentro da def.
"""

# Para utilizar essa função precisamos chamá-la
diz_oi()

# Veja que nunca podemos esquecer de usar o parênteses ao executar uma função. Lembrar também que ele é COLADO à função.
print('-----')


def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data')
    print('Querida')
    print(' ')


# Chamando 3 vezes a mesma função.
cantar_parabens()
cantar_parabens()
cantar_parabens()
print('-----')


# or

for n in range(5):  # executando 5 vezes. A posição é n-1.
    cantar_parabens()
print('-----')

# or, mas não recomendado. Criando variáveis do tipo função. Executamos a variável como função.

cantar = cantar_parabens  # recebe a execução. Veja que não temos o parênteses. Esse método NÃO é comum.
cantar()
