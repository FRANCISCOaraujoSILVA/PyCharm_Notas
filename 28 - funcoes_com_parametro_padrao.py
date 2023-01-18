"""
                                FUNÇÕES COM PARÂMETRO PADRÃO (DEFAULT PARAMETERS)


- Funções onde a inserção do parâmetro é opcional
- '==' representa igualdade, igual ao matlab

Quais tipos de dados podemos utilizar como valores default para parâmetro?
    - qualquer tipo: números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc...
"""

print('Francisco Araújo')
print()  # Veja que a inserção de parâmetro para o print é opcional


def quadrado(numero):  # Inserção obrigatória
    return numero ** 2


print(quadrado(3))  # Ok
# print(quadrado())  # Veja que aqui a inserção de parâmetro é obrigatória


def exponencial(numero=4, potencia=2):  # veja que agora não precisamos inserir nenhum argumento, teremos 4^2
    return numero ** potencia


"""
Na definição de um método, dizer que um parâmetro é igual a algo (2 por exemplo), faz ele ser opcional. Veja que essa
sacada é muito simples, mas muito importante.
"""

print(exponencial(2, 3))  # OK
print(exponencial(2))  # OK
print(exponencial())  # OK
print('-----')

"""
A ordem dos argumentos importa.
OBS.: EM FUNÇÕES PYTHON, OS PARÂMETROS COM VALORES DEFAULT, DEVEM SEMPRE ESTAR AO FINAL DA DECLARAÇÃO.
"""

# def quadrado(num=2, potencia):  # Errado
#    return num ** potencia
# print(2) Poderíamos até pensar que esse 2 vai para a potência, mas não vai, pois o parâmetro default deve estar no fim

# Exemplo mais completo


def mostra_informacao(nome='Francisco', instrutor=False):  # Dois parâmetros não obrigatórios
    if nome == 'Francisco' and instrutor:  # E instrutor for True
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


def mat(num1, num2, fun=soma):  # Esse modo de programar não é comum em outras linguagens
    return fun(num1, num2)  # Aqui já estamos usando a função soma() como paradigma


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))  # Veja, que aqui estamos usando a função soma()
print(mat(2, 3, subtracao))  # Aqui estamos usando a função subtração(). Além disso, veja que a função subtração()
# está sem parênteses
print('-----')

# Exemplos de escopo de variável. Variáveis Globais e Variáveis Locais. Modo de evitar alguns problemas

instrutor = 'Petróleo'  # Exemplo de variável global. Pois está fora da função


def diz_oi():

    instrutor = 'Engenharia'  # Dentro da função

    """
    - Exemplo de variável local, veja que ela se sobressai em relação global. Veja que ela também está marcada
    - Essa variável local só existe dentro desse bloco, nem adianta chamar ela dentro de um print que esteja fora do 
    bloco que ela não vai existir
    """
    return f'oi {instrutor}'  # Esse return é muito legal


print(diz_oi())
print('-----')

# A dica é, evitar variável global, usar apenas se tiver confiança para usar

# Outro exemplo, para trabalhar com variáveis globais


total = 0


def incremento():
    global total  # Avisanso ao Python que a variável é a global (que está lá fora). Uma forma de inicializar a variável
    total = total + 1  # Se a inicialização gerar um UnbooundLocalError
    return total

# A declaração global se parece com o VBA do excel


print(incremento())
print(incremento())
print(incremento())  # Legal, aqui fica tipo um for
print('-----')

"""
- Podemos ter funções que podem ser declaradas dentro de funçoes, além de ter uma forma especial de escopo de variável
- É um jeito diferente de usar uma variável fora do escopo

Não é comum, mas é importante saber
"""


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Veja que "contador" não é local, não é global, É A VARIÁVEL QUE ESTÁ NA FUNÇÃO ANTERIOR
        # nonlocal diz que a variável está na função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

#  print(dentro()) # Veja que só existe no escopo da função fora(), a função dentro() não roda sozinha. Gera NameError
