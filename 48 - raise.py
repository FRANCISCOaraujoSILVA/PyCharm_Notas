"""
                                                        RAISE


- Levantamos os próprios erros com o raise
- Raise: não é uma função, é uma palavra reservada assim como o def. O raise gera erros
- O raise é útil quando queremos criar nossas próprias excessões e mensagens de erros

Forma geral:
    raise TipoDoErro('mensagem de erro')

Nota:
- O raise, assim como o return, finaliza nossa função/bloco
"""

# Exemplo


def colore(texto, cor):
    cores = ['azul', 'branco', 'amarelo', 'verde']
    if type(texto) is not str:  # Validação
        raise TypeError('Texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f"O texo: '{texto}', será impresso na cor: '{cor}'")


colore('Hoje é sexta-feira', 'azul')
# colore('Mais um dia', 2)  # Gera um erro
# colore('Hoje é sexta-feira', 'preto')  # Gera um erro

