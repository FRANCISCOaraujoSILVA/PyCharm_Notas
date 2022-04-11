"""
KWARGS:

-Entendendo o **kwargs: É apenas uma convenção. Vai funcionar desde que tenha "**". Usado para parâmetros extras
-É apenas uma parâmentro
-Exige que utilizemos parâmetros nomeados. Esses parâmetros são transformados em um dicionário
-Tanto o *args quando o **kwargs não são obrigatórios
-naturalmente, o ** desempacota
-ao usar dicionários em uma função, cuidado! os nomes da chave em um dicionário devem ser os mesmos dos parâmetros
da função

"""
# Exemplo 1:


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}!')


cores_favoritas(eu='Azul', ela='preto', nos='azul escuro')  # Vai criar o dicionário
cores_favoritas()  # Não gera erro
cores_favoritas(Francisco='Araújo')

# Exemplo 3
print('-----')


def cumprimento_especial(**kwargs):
    if 'Francisco' in kwargs and kwargs['Francisco'] == 'Araújo':  # se a chave estiver no dicionário e valor for Ara...
        return 'Você recebeu um comprimento direto de Francisco Araújo!'
    elif 'Francisco' in kwargs:  # Se a chave estiver no dicionário
        return f"{kwargs['Francisco']}, é o sobrenome do Fracisco"
    return 'Não faço ideia de quem seja você!'


print(cumprimento_especial())
print(cumprimento_especial(Francisco='Araújo'))
print(cumprimento_especial(Francisco='Almeida'))
print(cumprimento_especial(Francisco='Silva'))

"""
Em suma, nas nossas funções podemos ter (nesta ordem - se for usar todos):
- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs
"""
# Vejo o exemplo abaixo. Podemos ter no mesmo argumento, tipos repetidos de parâmetro.
print('-----')


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
print('-----')
print(minha_func('Francisco', 25, curso='Engenha', espec='Petróleo'))  # Os dois últimos vão para **kwargs


# Desempacotar com o **kwargs
print('-----')


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Francisco', 'sobrenome': 'Araújo'}  # É aquela outra forma de criar dicionário

# print(mostra_nomes(nomes))  # Gera erro, pois não tem como desempacotar assim
print(mostra_nomes(nome='Eu', sobrenome='Araújo'))  # ok
print(mostra_nomes(**nomes))  # Pythônico
