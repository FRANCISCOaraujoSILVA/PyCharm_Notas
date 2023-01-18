"""
DEBUGANDO COM PDB

PDB: Python Debugger
Bub: inseto

É importante saber qual o valor de uma variável em determinado ponto.
"""
# Forma amadora


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu algum problema: {err}'


print(dividir(4, 7))

# Exemplo com o PyCharm (break point)
"""
Para isso, dê um break point na linha 34 e 36, depois clique na joaninha. Depois perceba os valores dos argumentos
na frente da def.
Você pode selecionar "int(a) / int(b)", clicar com o botão direito, selicionar Add To Watches para ver o resultado da 
execução do código. Além disso, pode clicar no ócular para criar outra janela.

F8 para pular as linhas durante a execução do debugging
"""
print('-----')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu algum problema: {err}'


print(dividir(4, 7))

# Exemplo com o PDB - Python Debugger (para qualquer IDE)
"""
Precisamos* importar a biblioteca pdb e então utilizar a função set_trace(). Nesse caso, podemos clicar apenas no run.
Comandos básicos do PDB
l: lista onde estamos no código
n: próxima linha
p: imprime a variável
c: continua a execução - finaliza o debugging
"""

"""
# Exemplo 1

import pdb

nome = 'Francisco'
sobrenome = 'Araújo'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# Exemplo 1 - Novidade, quando queremos executar dois comandos em uma mesma linha devermos separar por ponto e vírgula.


nome = 'Francisco'
sobrenome = 'Araújo'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


"""
Explicando o asterisco na linhas 47. A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o 
comando de debug foi incorporado como função built-in (integrado) chamado breakpoint()
"""
print('-----')

# Exemplo 2 - Aplicando com a nova função função integrada do Python (breakpoint()) - Veja que surge EOF

nome = 'Francisco'
sobrenome = 'Araújo'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
print('-----')

# Nota: Cuidado com conflitos entre nomes de veriáveis e os comandos do pdb
# Exemplo 3 - Antes, para imprimir algo deveríamos digitar o nome da variável. Agora (p nomeVariável)


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 5))

