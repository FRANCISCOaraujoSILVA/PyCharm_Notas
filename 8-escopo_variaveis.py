"""
ESCOPO DE VARIÁVEIS:

Escopo é a limitação de algo. Ou seja, onde que nossa variável vai ser reconhecida dentro do nosso código. Temos dois
casos:

VARIÁVEIS GLOBAIS: seu escopo compreende no programa inteiro

VARIÁVEIS LOCAIS: reconhecidas apenas no bloco onde foram declaradas

Para declarar variáveis em python:

Nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica, ou seja, quando declaramos uma variável, não colocamos o tipo de dado dela.

Se fosse em linguagem C:
int numero = 42

Se fosse em linguagem Java:
int numero = 42

Nessas linguagens, uma vez que a variável é declarada não podemos mais mudar. No entanto, aqui no python
podemos fazer retribuição, por isso, dinâmica

if numero > 10:
    novo = numero + 10
    print(novo)  # Dentro do bloco

print(novo)  # Fora do bloco

Veja que a variável novo está apenas dentro do laço. Ou seja, ela só existe lá, por isso ela é uma variável local
"""

numero = 42  # exemplo de variável global, posso acessar em qualquer parte do código
print(numero)
print(type(numero))
print('-----')

if numero > 10:
    novo = numero + 10
    print(novo)  # ela vai existir aqui dentro

# um exemplo de variável de escopo não global é aquela que pode estar dentro de um if apenas, por exemplo.
