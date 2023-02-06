"""
                                                MODOS DE ABERTURA DE ARQUIVO


- r: Abre para leitura
- w: Abre para escrita (sobrescreve caso o arquivo já exista)
- x: Abre para escrita somente se o arquivo não existir
- a: Abre para escrita e adiciona o conteúdo ao final do arquivo (tipo a função append()). Um arquivo é criado se não
existir e, se existir, o conteúdo será adicionado. ESSE É MUITO INTERESSANTE
- Visite o site para descobrir novos modos de abertura: http://docs.python.org/3/library/functions.html#open

E para escrever no início do arquivo?
Não sei ainda. Nem adianta usar seek(0). Me parece que sempre será adicionado no começo.

Tentei os comandos abaixo mas não adiantou.
with open('62a - novo.txt', 'a', encoding='UTF-8') as arkiu:
    arkiu.seek(0)  # Não adianta
    arkiu.write('Escrevendo no começo!')
"""

# with open('63a - beach.txt', 'x', encoding='UTF-8') as qualquer:
#     qualquer.write('Teste de conteúdo.\n')
# Ou seja, a aplicação é executada apenas uma vez. Num próximo run gera erro
# print('-----')

# Refatorando o código para não gerar erro

try:
    with open('63a - beach.txt', 'x', encoding='UTF-8') as qualquer:
        qualquer.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existente!')  # Gera um aviso
print('-----')

"""
with open('62c - frutas', 'a', encoding='UTF-8') as arq:
    while True:
        fruta = input("Digite a fruta que deseja adicionar ou digite 'sair' para finalizar: ")
        if fruta != 'sair':
            arq.write('- '+fruta + '\n')   # ('\n') Coloca a fruta na linha seguinte
        else:
            break
"""
