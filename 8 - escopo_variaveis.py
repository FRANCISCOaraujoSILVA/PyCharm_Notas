"""
                                            ESCOPO DE VARIÁVEIS


Escopo é a limitação de algo. Ou seja, o local nossa variável será reconhecida dentro do nosso código. Temos dois
casos:

    - VARIÁVEIS GLOBAIS: seu escopo compreende no programa inteiro
    - VARIÁVEIS LOCAIS: reconhecidas apenas no bloco onde foram declaradas

Para declarar variáveis em python:
    - Nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica, ou seja, quando declaramos uma variável, não determinado qual tipo de dado
ela é.

Linguagens onde é necessário declarar o tipo de dado.
        Se fosse em linguagem C:
        int numero = 42

        Se fosse em linguagem Java:
        int numero = 42

Nessas linguagens, uma vez que a variável é declarada, não podemos mudar. No entanto, aqui no python podemos fazer
retribuição, por isso é uma linguagem de tipagem dinâmica.

Por exemplo:

if numero > 10:
    novo = numero + 10
    print(novo)  # Dentro do bloco

print(novo)  # Fora do bloco

Veja que a variável 'novo' está apenas dentro do laço. Ou seja, ela só existe lá, por isso ela é uma variável local.

Nota:
Um exemplo de variável de escopo não global é aquela que pode estar dentro de um if apenas, por exemplo.
"""

numero = 42  # Exemplo de variável global. Posso acessar essa variável em qualquer parte do código
print(numero)
print(type(numero))
print('-----')

if numero > 10:
    novo = numero + 10
    print(novo)  # Ela vai existir apenas aqui dentro do código
