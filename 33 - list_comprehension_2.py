"""
LIST COMPREHENSION PARTE 2:

Podemos adicionar estrutrua condicionais lógicas às nossas List Comprehension

# Sintaxe
[dado for dado in coleção condição]
"""

#  Exemplo 1: verifica os pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Os pares: {[dado for dado in numeros if dado % 2 == 0]}')

"""
Ou seja, estamos dizendo que:
Pegamos o dado, para cada dado na coleção se o resto da divisão desse dado por 2 for 0 (condição de paridade).
"""

#  Exemplo 2: verifica os ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Os ímpares: {[dado for dado in numeros if dado % 2 != 0]}')
print('------')


# Refatorado:
"""
Quando o número é par, o módulo de 2 é zero. Zero em Python é False. A Condiçao not
gera False = True. Vai salvar os True, que são os pares (False).
Estamos fazendo uma negação.
"""
print(f'Os pares: {[nume for nume in numeros if not nume % 2]}')

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True. Vai salvar os True. Nem precisa de negação.
print(f'Os pares: {[nume for nume in numeros if nume % 2]}')


# Exemplo 3: condição no início
print(f'Modificando: {[numero**numero if numero % 2 == 0 else numero/numero for numero in numeros]}')
print('-----')
