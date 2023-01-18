"""
LEITURA DE ARQUIVOS:

Para ler o conteúdo de uma arquivo em Python, utilizamos a função integrada open(). Por padrão, já está no modo de
leitura "r"

open(): Na forma mais simples de utilização passamos apenas um parâmetro de entrada, que nesse caso é caminho do arquivo
a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalharemos

https://docs.python.org/3/library/functions.html#open

Obs.: por padrão, a função open() abre o arquivo para leitura. Esse arquivo deve existir, caso contrário
teremos o erro  FileNotFoundError

"""
# Exemplo:
arquivo = open('59a - texto.txt', encoding='UTF-8')  # Por padrão, my escrita não era "UTF-8", por isso tive que forçar
print(arquivo)
# ret = arquivo.read()  # O parâmetro (posição) do read sinaliza até onde queremos ler. Lá o cursor fica parado
# print(type(ret))  # Tipo string
print('-----')
"""
<_io.TextIOWrapper name='59a - texto.txt' mode='r' encoding='cp1252'>
name: nome do arquivo
'r': indica que é apenas um modo de leitura. r: read(), ou seja, apenas para ler
encoding: diz respeito a atualização. Não é importante. Mas o padrão seria UTF-8 (99,9% dos casos)
"""
print(type(arquivo))
print('----')


# Para ler o conteúdo de um arquivo após a abertura
print(arquivo.read())  # ele lê a primeira linha e o cursor fica no fim
print(arquivo.read())  # Não vai repetir o print porque o cursor já está no fim.
# Ou seja, não tem nada do fim pra frente
