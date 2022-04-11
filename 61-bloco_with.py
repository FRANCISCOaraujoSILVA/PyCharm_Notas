"""
BLOCO WITH:

O bloco with - Para não precisar fazer o fechamento do arquivo. Dentro do with está aberto! Fora está fechado

Passos para se trabalhar com arquivo:
1 - abrir o arquivo
2 - manipular o arquivo
3 - fechar o arquivo (nós, manualmente)

O bloco with é usado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.
"""

# o bloco with
with open('59.1-texto.txt', encoding='UTF-8') as arquivo:  # forma pythônica de trabalhar com arquivos
    print(arquivo.readlines())  # imprime cada linha como um elemento da lista

# print(arquivo.readlines())  # a operação não existe fora do with
