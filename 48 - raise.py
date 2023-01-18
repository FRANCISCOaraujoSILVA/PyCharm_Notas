"""
RAISE

Levantando os próprios erros com o raise.

raise: não é uma função, é uma palavra reservada assim como o def. O raise gera erros
O raise é útil quando queremos criar nossas próprias excessões e mensagens de erros.

Forma geral:

raise TipoDoErro('mensagem de erro')

Nota: O raise, assim o return, finaliza nossa função.
"""

# raise ValueError('Valor incorreto')

# Exemplo real


def colore(texto, cor):
    cores = ['azul', 'branco']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f"O texo: '{texto}', será impresso na cor: '{cor}'")


colore('Hoje é sexta-feira', 'azul')



