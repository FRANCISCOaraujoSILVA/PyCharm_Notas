"""
ESCOPO DE VARIÁVEIS:

Escopo é a limitação de algo. Ou seja, onde que nossa variável vai ser reconhecida dentro do nosso código. Temos dois
casos.

VARIÁVEIS GLOBAIS: seu escopo compreende no programa inteiro

VARIÁVEIS LOCAIS: reconhecidas apenas no bloco onde forma declaradas

Para declarar variáveis em python:

Nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica, ou seja, quando declaramos uma variável, não colocamos o tipo de dado dela.

Se fosse em C:
int numero = 42
Se fosse em Java:
int numero = 42

Nessas linguagens, uma vez que a variável é declarada não podemos mais mudar. Já aqui no python
podemos fazer retribuição.

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)

Veja que a variável novo está apenas dentro do laço.
"""

numero = 42  # exemplo de variável global, posso acessar em qualquer parte do código
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10
    print(novo)


# um exemplo de variável de escopo não global é aquela que pode estar dentro de um if apenas, por exemplo.
