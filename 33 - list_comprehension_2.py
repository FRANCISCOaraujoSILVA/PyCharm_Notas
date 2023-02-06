"""
                                        LIST COMPREHENSION - PARTE 2


- Podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

Sintaxe:

[dado for dado in coleção condição]: Observe que agora podemos inserir uma condição
"""

#  Exemplo 1: Verifica os pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Os pares: {[dado for dado in numeros if dado % 2 == 0]}')
print('------')

"""
Ou seja, estamos dizendo que:
Pegamos o dado, para cada dado na coleção se o resto da divisão desse dado por 2 for 0 (condição de paridade).
"""

#  Exemplo 2: Verifica os ímpares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Os ímpares: {[dado for dado in numeros if dado % 2 != 0]}')
print('------')

# Refatorado:

"""
Quando o número é par,  %2 é 0, e 0 em Python é False. A condiçao not gera False = True. Logo, vai 
salvar os True, que são os pares. Estamos fazendo uma negação. Se pareceu complicado veja o código abaixo.
"""

print(f'Os pares: {[nume for nume in numeros if not nume % 2]}')
# print(2 % 2)  # Veja que o resto da divisão por 2 é 0 (False)
# print(not 2 % 2)  # Vira True ao fazer a negação. Logo, se for True é porque o número é par

"""
A condição 'if not nume % 2' diz: Se o resto da divisão de num por 2 for zero, transforme em True e pegue o dado.
"""

# Quando o número é ímpar, %2 é 1, e 1 em Python é True. Vai salvar os True, que são os ímpares

print(f'Os ímpares: {[nume for nume in numeros if nume % 2]}')
print('-----')

# Exemplo 3: Condição no início

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Modificando: {[numero**numero if numero % 2 == 0 else numero/numero for numero in numeros]}')

"""
Ou seja, se o resto da divisão de numero por 2 for 0: numero^numero
Se não: fazemos numero/numero
"""
