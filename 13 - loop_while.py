"""
                 LOOP WHILE - É IMPORTANTE LEMBRAR DA EXPRESSÃO BOOLEANA E O CRITÉRIO DE PARADA


Forma geral:
while expressão_booleana:
    //execução do loop

- O bloco while se repete enquanto a expressão BOOLEANA for verdadeira
- Expressão BOOLEANA é toda expressão onde o resultado é verdadeiro ou falso

ex.:
num = 5
Análise:
num < 5    False
num < 10   True

Ou seja, condições de verdadeiro ou falso.
"""

# Exemplo 1

numero = 10
while numero > 0:  # Ou seja, enquanto o 'numero' for maior que 0, executamos o código
    print(f'O número da vez é: {numero}')
    numero = numero - 1
print('-----')

"""
Obs.: Em um loop while é importante cuidar do critério de parada. Se a condição não for satisfeita, para "parar" é 
preciso clicar no stop do RUN.
"""

# Exemplo 2

resposta = ''  # Ou seja, o input da nossa variável será uma string
while resposta != 'sim' and resposta != 'Sim':  # Um modo de cobrir as duas possibilidades para S minúsculo e maiúsculo
    resposta = input('Já finalizou Francisco???: ')

print('Parabéns por ter finalizado Francisco!')  # Mensagem de saída quando o loop é finalizado
