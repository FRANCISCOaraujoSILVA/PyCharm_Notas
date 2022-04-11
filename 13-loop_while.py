"""
LOOP WHILE: É IMPORTANTE LEMBRAR DA EXPRESSÃO BOOLEANA E O CRITÉRIO DE PARADA.

Forma geral:
while expressão_booleana:
    //execução do loop

O bloco do while se repete enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso!

ex.:
num = 5
num < 5    False
num < 10   True

Ou seja, condições de verdadeiro ou falso.
"""
# Exemplo 1:

numero = 10

while numero > 0:  # eu que escolhi essa forma de decréscimo
    print(f'O número da vez é: {numero}')
    numero = numero - 1
print('-----')

# Obs.: Em um loop while é importante cuidar do critério de parada. Para "parar" é preciso clicar no stop do RUN, se o
# código for acionado aqui no script.


# Exemplo 2:

resposta = ''

while resposta != 'sim' and resposta != 'Sim':  # um jeido de cobrir as dus possibilidades para S Minúsculo e Maiúsculo
    resposta = input('Já finalizou Francisco???: ')
