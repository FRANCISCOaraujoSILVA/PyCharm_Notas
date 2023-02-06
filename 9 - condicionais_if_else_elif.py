"""
                                                ESTRUTURAS CONDICIONAIS

Temos:
    - if
    - else
    - elif (para mais de duas estruturas condicionais)
        - elif = else+if. Se parece muito com o elseif do matlab
"""

idade = 15

if idade < 18:  # Veja que os dois pontos cria o bloco, e para o if a estrutura condicional é na frente
    print('Menor de idade!')
    print(f'{idade} anos')
elif idade == 18:  # Estrutura condicional na frente para o elif. Podemos ter vários "elifs"
    print('Tem 18 anos')
else:  # Estrutura condicional em baixo para o else
    print('Maior de idade!')
    print(f'{idade} anos')

"""
Note que no Python é muito mais limpo para escrever estruturas condicionais. Além disso, podemos ter vários "ifs" 
também, mas não é legal, pois fica muito poluído visualmente. Enfim, não é elegante.
"""
