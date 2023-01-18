"""
                                                    TIPO STRING


Sempre que:
- Estiver entre aspas simples
- Estiver entre aspas duplas
- Estiver entre aspas simples triplas
- Estiver entre aspas duplas triplas
- Dados de input

Nota:
O mais comum é usar aspas simples.
Se quisermos pular uma linha dentro de uma string, basta colocar: \n

A primeira posição de uma lista é o 0, diferente do MatLab que inicia com 1.
"""

nome = 'Francisco \nAraújo \nda \nSilva'
print(nome)
print(type(nome))
print('-----')

# Podemos fazer assim também, mas tem que ser com três aspas duplas

nome1 = """Pulando
Francisco
Araújo
da
silva
"""
print(nome1)
print(type(nome1))
print('-----')

nome2 = "Francisco \"Araújo\" "  # Uma maneira elegante de inserir aspas dentro de uma string
# print(nome2.lower())  # Transforma tudo em minúsculo
print(nome2)
print('-----')

print(nome2[0:9])  # Uma maneira de capturar um dado, conhecido como Slice de String
print(nome2.split())  # Transforma a variável 'nome2' em uma lista de string ['Francisco', '"Araújo"']
print(nome2.split()[0])  # Pegamos o primeiro elemento dessa lista, já que o "0" é a primeira posição
print(nome2.split()[1])  # Pegamos o segundo elemento da lista
print('-----')

# Invertendo as letras de uma string

print(nome2[::-1])  # Ou seja, vamos do primeiro até o último (::) e invertemos (-1)
print('-----')

# Podemos também trocar uma letra por outra
print(nome.replace('F', 'FF'))  # Ou seja, trocamos F por FF
print('-----')

texto = 'socorram me subino onibus em marrocos'  # Palíndromo. haha legal
print(texto)
print(texto[::-1])
print('-----')

print("""Francisco "Araújo" """)  # Outro Jeito de escrever aspas dentro de uma string
