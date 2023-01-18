"""
MÉTODOS MÁGICOS

Não tem muita relação com programação orientada a objetos.

Métodos mágicos são todos os métodos que utilizam dunder (utilizam Double UNDERscore).
    - dunder repr: representação do objeto (geralmente apenas para o desenvolvedor)
    - dunder str: tem preferencia de representação
    - dunder len
    - dunder del  (faça o teste no terminal)
    - dunder add


No terminal faça: dir(__builtins__)
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro1 = Livro('Um navio não foi feito para estar na costa', "Desconhecido", 300)
livro2 = Livro('Um livro sobre empatia', "População", 5000)

print(livro1)  # endereço de memória
print(livro2)  # endereço de memória
print('-----')

"""
Podemos sobrescrever este objeto para nos mostrar informações mais relevantes além do endereço de memória.
    - Usando o método mágico: __reper__
"""


class NovoLivro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return self.titulo  # estamos representando apenas o título

    def __str__(self):  # tem preferência na execução. Ou seja, __repr__ não será executado
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        return 'Um objeto foi apagado'

    def __add__(self, other):
        return f'{self} - {other}'  # self é o primeiro elemento


livro3 = NovoLivro('Um navio não foi feito para estar na costa', "Desconhecido", 300)
livro4 = NovoLivro('Um livro sobre empatia', "População", 5000)

print(livro3)  # melhor representação das informações
print(livro4)
print('-----')

print(len(livro3))
print(len(livro4))
print('-----')

print(livro3 + livro4)  # aplicando o add. Fazendo uma operação. O add é o sinal de '+'
