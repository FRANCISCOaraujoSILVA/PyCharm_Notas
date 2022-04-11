"""
ESCREVENDO EM ARQUIVOS:

 - Quando abrimos para leitura, podemos apenas ler, sem escrever
 - Quando abrimos pra escrita, pdemos apenas escrever, sem ler
 - Para ler ou escrever precisamos abrir o arquivo
 - Abrimos com o open, mas agora, não no formato leitura "r"

-Quando abrimos no formato escrita, um arquivo é criado no sistema operacinal
-A função write recebe apenas string como parâmetro

Obs.: Na escrita:
Abrindo um arquivo para escrita  como o modo 'w': se o arquivo não existir um será criado; caso ele já exista, o
anterior será apagado
"""

# exemplo. Precisamos criar um novo arquivo.
with open('62.1-novo.txt', 'w', encoding="UTF-8") as arquivo:  # w: write
    arquivo.write('Podemos acrescentar uma linha no texto. \n')
    arquivo.write('Podemos acrescentar outra. \n')
    arquivo.write('Podemos acrescentar quantas quisermos. \n')
    # arquivo.write(2) TypeError, pois só aceita string

# Escrevendo várias vezes o mesmo arquvivo
print('-----')

with open('62.2-novoArquivo', 'w', encoding='UTF-8') as novoarquivo:
    novoarquivo.write('Francisco Araújo\n'*100)

# Recebendo dados do usuário e escrevendo
with open('62.3-Frutas', 'w', encoding='UTF-8') as arq:
    while True:
        fruta = input("Digite a fruta que deseja adicionar ou digite 'sair' para finalizar: ")
        if fruta != 'sair':
            arq.write('-'+fruta + '\n')   # or na próxima linha: arq.write('\n')
        else:
            break

print('-----')

