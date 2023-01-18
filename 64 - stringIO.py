"""
STRINGIO:

StringIO: Utilizado para ler e criar arquivos EM MEMÓRIA, pois nem sempre temos permissão para ler um arquivo

Para ler ou escrever em um arquivo do sistema operacional, é preciso ter permissão:
    -Permissão para leitura: Podemos ler o arquivo
    -Permissão para Escrita: Para criar o arquivo

EM MEMÓRIA: pois não vai gravar no disco, vai ficar apenas na memória do computador.
"""

# Primeiro: Fazemos o import
from io import StringIO  # no módulo  io import a função StrngIO

mensagem = 'É uma primeira mensagem que ficará em memória. Parece sentimento póstumo, mas é apenas um procedimento.'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para depois inserismos texto
arquivo = StringIO(mensagem+'\n')  # criando um arquijo já com um texto dentro dele

# é equivalente a: arquivo = open('arquivo.txt', 'w'), nesse caso, um arquivo (arquivo.txt) é criado

# Tendo o arquivo, agora, podemos manipular o mesmo normalmente.
print(arquivo.read())  # Veja que nenhuma arquivo será criado. Apenas criado em memória. A leitura foi feita em memória

# Inserindo novo texto
arquivo.write('Outro texto...')  # veja que será escrito no final da variável "arquivo"
print('-----')

# Podemos até manipular o cursor
arquivo.seek(0)  # cursor no início do arquivo
print(arquivo.read())

"Um diferencial da stringIO é que podemos abrir para escrita e leitura rapidamente."
