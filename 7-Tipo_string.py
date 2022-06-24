"""
TIPO STRING:

Sempre que:
- estiver entre aspas simples
- aspas duplas
- aspas simples triplas
- aspas duplas triplas
- dados de input

O mais comum é usar aspas simples.
Se quisermos pular uma linha dentro de uma string, basta colocar: \nFrancisco

A primeira posição de uma lista é o 0, diferente do MatLab.
"""

nome = 'Francisco \nAraújo \nda \nSilva'
print(nome)
print(type(nome))
print('-----')

# Podemos fazer assim também, mas tem que ser com duplas triplas

nome1 = """Francisco
Araújo
da
silva
"""
print(nome)
print(type(nome))
print('-----')

nome2 = "Francisco \"Araújo\" "  # Uma maneira elegante de inserir aspas dentro de uma string.
# print(nome2.lower()) Transforma tudo em minúsculo.
print(nome2)
print('-----')

print(nome2[0:9])  # Forma de capturar um dado, conhecido como Slice de string
print(nome2.split())  # Transforma os nomes em uma lista
print(nome2.split()[0])  # Pegamos o primeiro elemento dessa lista, já que o "0" é a primeira posição
print(nome2.split()[1])  # pegamos o segundo elemento da lista
print('-----')

# invertendo as letras

print(nome2[::-1])  # Ou seja, vamos do primeiro até o último e invertemos.
print('-----')

# Podemos também trocar uma letra por outra
print(nome.replace('F', 'FF'))  # Ou seja, trocamos F por FF
print('-----')

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)
print(texto[::-1])
print('-----')

print("""Francisco "Araújo" """)  # Outro Jeito de escrever aspas dentro de uma string.
