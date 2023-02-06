"""
                                            TRY / EXCEPT / ELSE/ FINALLY


- Usar try/except é comum
- Usar else/finally não é comum

Quando saber que devemos tratar um erro? Dica:
    - Toda entrada de dado deve ser tratada!

Nota:
- A função do usuário é DESTRUIR seu sistema.
- Dica ao tratar erros: Tratar sempre no começo
"""

# Else: Executa a linha apenas se não ocorrer o erro. Podemos ter um else para cada exept

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou: {num}')
print('-----')

# Finally: O menos interessante

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido!')
else:
    print(f'Você digitou o número: {num}')
finally:
    print('Executando o finally')

"""
Nota:
- O bloco finally sempre será executado, independente se houve exceção ou não. Ou seja, no fim do dia, faz o mesmo papel 
se tiver apenas o print da linha 33. Experimente tirar o finally de lá
- Então, por que executá-lo? Para fechar ou desalocar recursos. Ou seja, para encerrar conexões de arquivos para escrita 
ou leitura, ou para encerrar conexão com um banco de dados por exemplo
"""

# Exemplo mais elaborado de tratamento de erro


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:  # Note que podemos compilar os erros ao invés de criar vários except
        return f'Ocorreu algum problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo númeor: ')

print(dividir(num1, num2))
