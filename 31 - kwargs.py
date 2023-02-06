"""
                                                    **KWARGS


- Entendendo o **kwargs: É apenas uma convenção. Vai funcionar desde que tenha "**". Usado para parâmetros extras
- É apenas uma parâmentro
- Exige que utilizemos parâmetros nomeados. Esses parâmetros são transformados em um dicionário
- Tanto o *args quando o **kwargs não são obrigatórios
- Naturalmente, o '**' desempacota os dados
- Cuidado ao usar dicionários em uma função! Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros
da função
"""

# Exemplo 1


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}!')


cores_favoritas(eu='Azul', ela='preto', nos='azul escuro')  # Vai criar o dicionário
cores_favoritas()  # Não gera erro
cores_favoritas(Francisco='Araújo')
print('-----')

# Exemplo 3


def cumprimento_especial(**kwargs):
    if 'Francisco' in kwargs and kwargs['Francisco'] == 'Araújo':
        # Se a chave estiver no dicionário e o valor for 'Araújo'
        return 'Você recebeu um comprimento direto de Francisco Araújo!'
    elif 'Francisco' in kwargs:  # Se a chave estiver no dicionário
        return f"{kwargs['Francisco']}, é o sobrenome do Fracisco"
    return 'Não faço ideia de quem seja você!'


print(cumprimento_especial())
print(cumprimento_especial(Francisco='Araújo'))
print(cumprimento_especial(Francisco='Almeida'))
print(cumprimento_especial(Francisco='Silva'))
print('-----')

"""
Em suma, em nossas funções podemos ter (nesta ordem):
- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs
"""

# Veja o exemplo abaixo. Podemos ter no mesmo argumento, tipos repetidos de parâmetro


def minha_func(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos!')
    print(sum(args))
    if solteiro:
        print('Solteiro')
    else:
        print('Pegando')
    print(kwargs)


numeroo = [2, 3, 4]
print(minha_func('Francisco', 25, *numeroo, True, Arg='dicionário'))
print(minha_func('Francisco', 25, curso='Engenha', espec='Petróleo'))  # Os dois últimos argumentos vão para  o **kwargs
print('-----')

# Desempacotar com o **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Francisco', 'sobrenome': 'Araújo'}  # É aquela outra forma de criar dicionário

# print(mostra_nomes(nomes))  # Gera erro, pois não tem como desempacotar assim
print(mostra_nomes(nome='Eu', sobrenome='Araújo'))  # Ok
print(mostra_nomes(**nomes))  # Pythônico
