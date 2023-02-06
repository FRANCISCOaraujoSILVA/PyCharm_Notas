"""
                                                ESCREVENDO EM ARQUIVOS


- Quando abrimos para leitura, podemos apenas ler, sem escrever
- Quando abrimos pra escrita, podemos apenas escrever, sem ler
- Para ler ou escrever precisamos abrir o arquivo
- Abrimos com o open(), mas agora, não no formato leitura 'r'
- Quando abrimos no formato escrita, um arquivo é criado no sistema operacional
- A função write ('w') recebe apenas strings como parâmetro

Obs.:
Na escrita:
    - Ao abrir um arquivo para escrita no modo 'w': Se o arquivo não existir ele será criado, caso ele já exista, o
    conteúdo do anterior será apagado
"""

# Exemplo. Precisamos criar um novo arquivo

with open('62a - novo.txt', 'w', encoding="UTF-8") as arquivo:  # w: write
    arquivo.write('Podemos acrescentar a primeira linha no texto. \n')
    arquivo.write('Podemos acrescentar a segunda linha no texto. \n')
    arquivo.write('Podemos acrescentar a terceira linha no texto. \n')
    # arquivo.write(2) # Gera TypeError, pois só aceita string

# Escrevendo várias vezes no mesmo arquivo

with open('62b - novo_arquivo', 'w', encoding='UTF-8') as novoArquivo:
    novoArquivo.write('Francisco Araújo\n'*100)

# Recebendo dados do usuário e escrevendo

with open('62c - frutas', 'w', encoding='UTF-8') as arq:
    while True:
        fruta = input("Digite a fruta que deseja adicionar ao carrinho ou digite 'sair' para finalizar: ")
        if fruta != 'sair':
            arq.write('- '+fruta + '\n')   # ('\n') Coloca a fruta na linha seguinte
        else:
            break
