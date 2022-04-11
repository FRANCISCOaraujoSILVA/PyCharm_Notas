"""
FUNÇÕES COM PARÂMETRO PADRÃO (Default Parameters):

- Funções onde a passagem de parâmetro seja opcional;
- == representa igualdade, igual ao matlab

Quais tipos de dados podemos utilizar como valores default para parâmetro?
 - qualquer tipo: números, strings, floats, booleanos, listas, tuplas, dicionários, funcções, etc...
"""
print('Francisco Araújo')
print()  # Veja que a passagem de parãmetro para o print é opcional


def quadrado(numero):  # Passagem obrigatória
    return numero ** 2


print(quadrado(3))  # ok
# print(quadrado())  # Veja que aqui a passagem de parâmetro é obrigatória


def exponencial(numero=4, potencia=2):  # veja que agora não precisamos de nenhume argumento, teremos 4 ** 2
    return numero ** potencia


"""
Na definição de um método, dizer que um parâmetro é igual a algo (2 por exemplo), faz ele ser opcional. Veja que essa
sacada é muito simples, mas muito importante
"""


print(exponencial(2, 3))  # ok
print(exponencial(2))  # ok
print(exponencial())  # ok

"""
A ordem dos argumentos importa
Obs.: Em funções Python, os parâmetros com valores default, DEVEM sempre estar ao final da declaração, ou seja:
"""


# def quadrado(num=2, potencia):
#    return num ** potencia
# print(2) Poderíamos até pensar que esse 2 vai para a potência, mas não vai, pois o parâmetro default deve estar no fim

# Exemplo mais completo:

print('-----')


def mostra_informacao(nome='Francisco', instrutor=False):  # dois parâmetros não obrigatórios
    if nome == 'Francisco' and instrutor:  # e instrutor for True
        return 'Bem-vindo instrutor Francisco'
    elif nome == 'Francisco':
        return 'Eu pensei que você era instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))  # Preciso escrever o nome "instrutor". Caso não, será atribuido ao "nome"
print(mostra_informacao('Ana'))  # Podemos fazer de dois jeitos
print(mostra_informacao(nome='Ana'))  # Podemos fazer de dois jeitos
print(mostra_informacao(True))  # Veja que essa variável agora atribuída ao nome

print('-----')


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):  # não é comum em outras linguagens
    return fun(num1, num2)  # aqui já estamos usando a função soma como paradigma


def subracao(num1, num2):
    return num1 - num2


print(mat(2, 3))  # veja, que aqui já estamos usando a função soma.
print(mat(2, 3, subracao))  # Aqui estamos usando a função subração. Além disso, veja que a função subtração está sem
# parênteses.


# Exemplos de escopo de variável. Variáveis Globais e Variáveis Locais. Evita problemas
print('-----')

instrutor = 'Petróleo'  # Exemplo de variável global. Pois está fora da função


def diz_oi():
    instrutor = 'Engenharia'  # dentro da função
    """
    Exemplo de variável local, veja que ela se sobressai em relação global, veja que ela também está marcada
    Essa variável local só existe dentro desse bloco, nem adianta chamar ela dentro de um print fora do bloco que 
    ela não vai existir
    """

    return f'oi {instrutor}'  # Esse return é muito legal


print(diz_oi())
# A dica é, evitar variável global, usar apenas se tiver confiança para usar.
# Outro exemplo, para trabalhar com variáveis globais


print('-----')
total = 0


def incremento():
    global total  # Avisanso ao Python que a variável é a global que está lá fora. Uma forma de inicializar a variável
    total = total + 1  # Se a inicialização gera um UnbooundLocalError.
    return total

# A declaração global se parece com o VBA do excel


print(incremento())
print(incremento())
print(incremento())  # Legal, aqui fica tipo um for

"""
Podemos ter funções que podem ser declaradas dentro de funçoes, além de ter uma forma especial de escopo de variável
Um jeito diferente de usar uma variável fora do escopo

Não é comum, mas é importante saber
"""
print('-----')


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Veja que "contador" não é local, não é global, É A VARIÁVEL QUE ESTÁ NA FUNÇÃO ANTERIOR
        # significa que está na função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

# print(dentro()) veja que só existe no escopo da função fora, a função dentro não roda sozinha. Gera NameError
