"""
LENDO ARQUIVOS CSV (COMMA SEPARATED VALUES)


- O separador para os dados é uma ","
- Em um arquivo CSV nem sempre teremos cabeçalho para nossos dados


"""

with open('lutadores.csv') as arquivoLeitura:
    dadosLidos = arquivoLeitura.read()
    print(type(dadosLidos))
    print(dadosLidos)

