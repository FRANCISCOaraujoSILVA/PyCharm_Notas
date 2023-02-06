"""
                                                LEITURA DE ARQUIVOS


- Para ler o conteúdo de uma arquivo em Python, utilizamos a função integrada open(). Por padrão, já está no modo de
leitura "r"
- Open(): Na forma mais simples de utilização passamos apenas um parâmetro de entrada, que nesse caso é o caminho do
arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalharemos

Nota:
- O arquivo a ser lido deve existir, caso contrário teremos o erro  FileNotFoundError
- Conheça outras formas de manipulação de arquivos: https://docs.python.org/3/library/functions.html#open
"""

# Exemplo

arquivo = open('59a - texto.txt', encoding='UTF-8')  # Por padrão, a escrita não era "UTF-8", por isso tive que forçar
print(arquivo)
# ret = arquivo.read()  # O parâmetro (posição) do read sinaliza até onde queremos ler. Lá o cursor fica parado
# print(type(ret))  # Tipo string
print('-----')

"""
<_io.TextIOWrapper name='59a - texto.txt' mode='r' encoding='cp1252'>
    - name: Nome do arquivo
    - 'r': Indica que é apenas um modo de leitura. R de read(), ou seja, apenas para ler
    - encoding: Diz respeito a atualização. Não é importante. Mas o padrão seria UTF-8 (99,9% dos casos)
"""

print(f'Veja o tipo do arquivo: {type(arquivo)}')
print('----')

# Para ler o conteúdo de um arquivo após a abertura

print(arquivo.read())  # Ele lê o conteúdo e posiciona o curso no fim do texto
print(arquivo.read())  # Não vai repetir o print porque o cursor já está no fim. Ou seja, não tem nada do fim pra frente
