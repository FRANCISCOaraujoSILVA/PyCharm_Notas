"""
Levantando os próprios erros com o raise.
raise: gera exceções nos nossos códigos
- raise não é uma função. É uma palavara reservada, como o def por exemplo.
- útil para criar nossas exceções e mensagens de erros

forma geral:
- raise TipoDoErro('Mensagem de erro')
- raise ValueError('Valor incorreto')

Obs.: O raise, assim como o return, finaliza a função
"""

# Exemplo real
# NÃO ESTAMOS TRATANDO ERRO, APENAS LANÇANDO EXCEÇÕES.


def colore(texto, cor):
    cores = ('azul', 'laranja', 'preto', 'cinza')
    if type(texto) is not str:  # validação
        raise TypeError('O Texto precisar ser uma string')  # Aplicação do raise
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:\n{cores}')
        # Qualquer comando após o raise não existe
    return f"O texto '{texto}' será impresso na cor {cor}."


"""
Obs.: Sem o return, devo chamar a função a função assim:
colore('Parâmetro', 'Parâmetro'). Se for usar no print nesse formato vai gerar None

Com o returne, devo chamar a função dentro do print, caso contrário, não vai funcionar.
"""

print(colore('Esse texto', 'azul'))
# colore(1, 'Amarelo')  # gera erro
# colore('O texto a ser pintanto', 1) # gera erro
