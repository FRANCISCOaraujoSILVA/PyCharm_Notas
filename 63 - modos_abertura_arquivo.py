"""
MODOS DE ABERTURA DE ARQUIVO:

r: abre para leitura
w: abre para escrita - sobrescreve caso o arquivo já exista.
x: abre para escrita somente se o arquivo não existir

http://docs.python.org/3/library/functions.html#open

a: abre para escrita, adiciona o conteúdo ao final do arquivo, como o append. Um arquivo é criado se não existir. Se
existir, será adicionado. ESSE É MUITO INTERESSANTE


E para escrever no início do arquivo?
Não sei ainda. Nem adianta usar seek(0). Me parece que sempre será adicionado no começo

with open('62a - novo.txt', 'a', encoding='UTF-8') as arkiu:
    arkiu.seek(0)  # Não adianta
    arkiu.write('Escrevendo no começo!')
"""
"""
with open('63a - beach.txt', 'x', encoding='UTF-8') as qualquer:
    qualquer.write('Teste de conteúdo.\n')


# Ou seja aplicação é executada apenas uma vez. Num próximo run gera erro

# Refatorando para não gerar erro
try:
    with open('63a - beach.txt', 'x', encoding='UTF-8') as qualquer:
    qualquer.write('Teste de conteúdo.\n')
except FileExsistsError:
    print('Arquivo já existe') # gera um aviso

"""


"""
with open('62c - frutas', 'a', encoding='UTF-8') as arq:
    while True:
        fruta = input("Digite a fruta que deseja adicionar ou digite 'sair' para finalizar: ")
        if fruta != 'sair':
            arq.write('-'+fruta + '\n')   # or na próxima linha: arq.write('\n')
        else:
            break
"""

