"""
Esse script foi criado com o objetivo de recolher todas as anotações feitas em aulas
"""
lista_arquivos = ['1-PEP8.py', '2-dir_e_help.py', '3-recebendo_dados_do_usuario.py', '4-Tipo_numerico.py',
                  '5-Tipo_float.py', '6-Tipo_booleano.py', '7-Tipo_string.py', '8.1-tipo_none.py',
                  '8-escopo_variaveis.py', '9.1-exercicios_sec4.py', '9-condicionais_if_else_elif.py',
                  '10-condicionais_and_or_not_is.py', '11.1-exercicios_sec5.py', '11-loop_for.py',
                  '12-Entendendo_e_explorando_ranges.py', '13-loop_while.py',
                  '14-saindo_de_loops_com_break.py', '15.1-exercicios_sec6.py', '15-listas.py', '16-tuplas.py',
                  '17-Dicionarios.py',
                  '18-mapas.py', '19-conjuntos.py', '20-mc_counter.py', '21-mc_defaultDict.py', '22-mc_orderedDict.py',
                  '23-mc_namedTuple.py', '24-mc_deque.py', '25.1-exercicios_sec7_part1.py',
                  '25.2-exercicios_sec7_part2.py', '25-definindo_funcoes.py', '26-funcoes_com_retorno.py',
                  '27-funcoes_com_parametros.py', '28-funcoes_com_parametro_padrao.py', '29-docstrings.py',
                  '30-args.py', '31-kwargs.py', '32.1-exercicios_sec8.py', '32-list_comprehension_1.py',
                  '33-list_comprehension_2.py',
                  '34-listas_aninhadas.py', '35-dictionary_comprehension.py', '36-set_comprehension.py',
                  '37-lambdas.py', '38-map.py', '39-filter.py', '40-reduce.py', '41-Any_All.py', '42-generators.py',
                  '43-sorted.py', '44-min_e_max.py', '59-leitura_de_arquivos.py', '60-seek_e_cursors.py',
                  '61-bloco_with.py', '62-escrevendo_em_arquivos.py', '63-modos_abertura_arquivo.py',
                  '64-stringIO.py']
leitura_completa = [open(dado, 'r', encoding='UTF-8') for dado in lista_arquivos]
leitura_completa = [dado.read() for dado in leitura_completa]


with open('301-Todas_as_notas.txt', 'w', encoding='UTF-8') as notass:
    for i in range(0, len(leitura_completa)):
        notass.write(leitura_completa[i] +
                     '-------------------------------------------------------------------------------------------------'
                     '----------------------\n')
