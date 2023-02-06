"""
                                                    BLOCO WITH


- O bloco with: Para não precisar fazer o fechamento do arquivo. Dentro do with está aberto! Fora do with está fechado!

Passos para se trabalhar com arquivo:
    - 1) Abrir o arquivo
    - 2) Manipular o arquivo
    - 3) Fechar o arquivo (nós, manualmente)

- O bloco with é usado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with
"""

# O bloco with

with open('59a - texto.txt', encoding='UTF-8') as arquivo:  # Forma pythônica de trabalhar com arquivos
    print(arquivo.readlines())  # Imprime cada linha como um elemento da lista

# print(arquivo.readlines())  # Note que esssa operação não existe fora do do bloco with
