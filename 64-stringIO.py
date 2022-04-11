"""
STRINGIO:

StringIO: Utilizado para ler e criar arquivos em memória, pois nem sempre temos permissão para ler um arquivo

Ter permissão:
    -Permissão para leitura: Podemos ler o arquivo
    -Permissão para Escrita: Para criar o arquivo
"""

# Primeiro: Fazemos o import
from io import StringIO

mensagem = 'É uma primeira mensagem que ficará em memória. Parece sentimento póstumo, mas é apenas um procedimento.'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem+'\n')
# é equivalente a: arquivo = open('arquivo.txt', 'w')

# Tendo o arquivo, agora, podemos manipular o mesmo normalmente.
print(arquivo.read())  # Veja que nenhuma arquivo será criado. Apenas criado em memória
print('-----')

# Inserindo novo texto
arquivo.write('Outro texto.')

# Podemos até manipular o cursor
arquivo.seek(0)
print(arquivo.read())
