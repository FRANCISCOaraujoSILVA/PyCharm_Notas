"""
                                                    STRINGIO


- StringIO: Utilizado para ler e criar arquivos EM MEMÓRIA, pois nem sempre temos permissão para ler um arquivo

Para ler ou escrever em um arquivo do sistema operacional, é preciso ter permissão:
    - Permissão para leitura: Podemos ler o arquivo
    - Permissão para Escrita: Para criar o arquivo

Nota:
- EM MEMÓRIA: pois não vai gravar o conteúdo no disco, vai ficar apenas na memória do computador
- Um diferencial da stringIO é que podemos abrir para escrita e leitura rapidamente

Achei essa parte muito interessante.
"""

# Primeiro: Fazemos o import

from io import StringIO  # No módulo io import a função StringIO

mensagem = 'É uma primeira mensagem que ficará em memória. Parece sentimento póstumo, mas é apenas um procedimento.'

# Podemos criar um arquivo em memória já com uma string inserida, ou mesmo vazio para depois inserirmos o texto

arquivo = StringIO(mensagem+'\n')  # Criando um arquivo em memória já com um texto dentro dele
# É equivalente a: arquivo = open('arquivo.txt', 'w'), nesse caso, um arquivo 'arquivo.txt' é criado no computador

# Tendo o arquivo, agora, podemos manipular o mesmo normalmente

print(arquivo.read())  # Veja que nenhum arquivo será criado. Existe apenas em memória. A leitura também é em memória

# Inserindo novo texto

arquivo.write('Outro texto...')  # Veja que será escrito no final da variável 'arquivo'
print('-----')

# Podemos até manipular o cursor

arquivo.seek(0)  # Cursor no início do arquivo
print(arquivo.read())
print('-----')
