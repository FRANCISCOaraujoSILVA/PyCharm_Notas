"""
                                                MÓDULO RANDOM


O que são módulos? Outros arquivos em Python.
Por que criar módulos? Para deixar o programa mais simples e para poder reutilizar o código.

Nota:
- Um módulo pode ser criado por qualquer programdar e também pode ser compartilhado na comunidade
- Um conjunto de módulos cria um pacote
- Módulo Random: Possui várias funções para gerar números pseudo-aleatórios (pseudo pois repete números)
"""

# Existem duas formas de utilzar um módulo ou função deste pacote

# Forma 1: Importanto todo o móudulo (não recomendado)

import random

# Random: gera um número pseudo-aleatório entre 0 e 1

""" 
Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades  que estiverem dentro do
módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções precisa usar deste módulo, vamos aprender
a buscar essa função no próximo exemplo.

Faça no terminal: import random, dir(random) e depois help(random.random) para abrir a documentação
"""

print(random.random())  # Primeiro é o nome do pacote e depois o nome da função que queremos usar (separados por '.')
# Nota: Ctrl+botãoEsquerdo no pacote random para vizualizar todas as funções contidas nesse pacote
print('-----')

# Forma 2: Importando uma função específica do módulo (recomendado)

# Digamos que queremos apenas a função random() desse pacote random

from random import random

# Ou seja, do pacote random queremos importar a função random. Perceba que os parênteses surgem apenas na execução.
# Veja também que na utilização não precisamos mais referenciar assim: random.random() para utilizar.


for i in range(10):  # Gera 10 números
    print(random())  # Usamos a função random() como se fosse nossa
print('-----')


# Forma 3: Função uniform(): gera números do tipo float pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):  # Gera 10 números
    print(uniform(3, 7))  # Lembre-se que o sete não será incluído
print('-----')

# Forma 4: Função randint(): Gera números do tipo int pseudo-aleatório entre os valores estabelecidos

from random import randint

for i in range(6):  # Gera 6 números
    print(randint(3, 7), end=',')  # Nesse caso, o sete será incluído. Vamos imprimir na mesma tela separados por ','
print('\n')
print('-----')

# Forma 5: Função choice(): Mostra um valor aleatório de um iterável. Legal essa função

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))  # Jogadas também poderia ser uma string (ele sortearia uma letra dessa string)
print('-----')

# Forma 7: função shuffle(): Embaralha os dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)  # Original
shuffle(cartas)
print(cartas)  # Após o embaralhamento
print(f'Sua carta: {cartas[0]}')

# Ou, podemos embaralhar e retirar a última carta para o usuário (tipo um sorteio mesmo)

print(cartas.pop())  # Lembra do pop? Ele retira e mostra o último elemento de uma lista
