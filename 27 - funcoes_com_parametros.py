"""
                                                FUNÇÕES COM PARÂMETROS


Entrada -> Processamento -> Saída
"""

# Refatorando uma função


def quadrado(numero):  # TypeError se o parâmetro não for informado
    # return numero * numero
     return numero ** 2


print(quadrado(10))
print(quadrado(20))
print(quadrado(30))
# Veja que o parâmetro no print é obrigatório.
print('------')

# Refatorando outra função


def cantar_para(Aniversariante):
    print(f'Parabéns {Aniversariante}')
    print('Nesta data')
    print('Querida')


cantar_para('Francisco')
print('-----')

# Exemplo com mais parâmetros


def somar(a, b):
    return a + b


def mult(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg
    # Veja que a mensagem vai se repetir pela quantidade da soma (num1 + b).
    # Lembrar que  3*'palavra' = palavra palavra palavra.


print(somar(2, 5))
print(somar(5, 5))

print(mult(2, 5))
print(mult(5, 5))

print(outra(2, 2, 'Francisco Araújo'))
print(outra(5, 5, 'Francisco Araújo'))
print('-----')

# Nomeando parâmetros, para facilitar a leitura do código para que deseja usar


def nome_completo(nome, sobrenome):  # Parâmetros (dados passados na definição da função)
    return f'Seu nome completo é {nome} {sobrenome}'  # Legal essa maneira de trabalhar com o print


print(nome_completo('Francisco', 'Araújo'))  # Argumentos (dados passados durante a execução da função)
print('-----')

"""
- A ordem dos parâmtros importa
- Argumentos nomeados (Keyword Arguments), podemos colocar na ordem que desejarmos. Parece muito vantajoso
- Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer nome
"""

nome = 'Lara'
sobrenome = 'Cristina'
print(nome_completo(nome='Francisco', sobrenome='Araújo'))  # Observe que os nomes em vermelho são os criados na def
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Stemckof', nome='Sara'))
print('------')

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # Veja que se dermos mais um tab, o if itera apenas uma vez, já que o return finaliza o passo


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
