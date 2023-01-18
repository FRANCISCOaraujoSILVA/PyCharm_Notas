"""
CRIANDO SUA PRÓPRIA VERSÃO DE LOOP

Por quê? Porque precisamos etender a fundo como esses laços funcionam.
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for([1, 2, 4, 5, 6])
