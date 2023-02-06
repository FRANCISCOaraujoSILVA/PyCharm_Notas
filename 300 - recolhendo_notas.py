"""
                ESSE SCRIPT FOI CRIADO COM O OBJETIVO DE RECOLHER TODAS AS ANOTAÇÕES FEITAS EM AULAS


"""

lista_arquivos = ['0 - cronograma_de_conteudos.txt', '1 - PEP8.py', '2 - dir_e_help.py',
                  '3 - recebendo_dados_do_usuario.py', '4 - tipo_numerico.py', '5 - tipo_float.py',
                  '6 - tipo_booleano.py', '7 - tipo_string.py', '8a - tipo_none.py', '8 - escopo_variaveis.py',
                  '9a - exercicios_sec4.py', '9 - condicionais_if_else_elif.py', '10 - condicionais_and_or_not_is.py',
                  '11a - exercicios_sec5.py', '11 - loop_for.py', '12 - entendendo_e_explorando_ranges.py',
                  '13 - loop_while.py', '14 - saindo_de_loops_com_break.py', '15a - exercicios_sec6.py',
                  '15 - listas.py', '16 - tuplas.py', '17 - dicionarios.py', '18 - mapas.py', '19 - conjuntos.py',
                  '20 - mc_counter.py', '21 - mc_defaultDict.py', '22 - mc_orderedDict.py', '23 - mc_namedTuple.py',
                  '24 - mc_deque.py', '25a - exercicios_sec7_part1.py', '25b - exercicios_sec7_part2.py',
                  '25 - definindo_funcoes.py', '26 - funcoes_com_retorno.py', '27 - funcoes_com_parametros.py',
                  '28 - funcoes_com_parametro_padrao.py', '29 - docstrings.py', '30 - args.py', '31 - kwargs.py',
                  '32a - exercicios_sec8.py', '32 - list_comprehension_1.py', '33 - list_comprehension_2.py',
                  '34 - listas_aninhadas.py', '35 - dictionary_comprehension.py', '36 - set_comprehension.py',
                  '37 - lambdas.py', '38 - map.py', '39 - filter.py', '40 - reduce.py', '41 - any_all.py',
                  '42 - generators.py', '43 - sorted.py', '44 - min_e_max.py', '45 - reversed.py',
                  '46 - len_abs_sum_round.py', '47 - zip.py', '48 - raise.py', '49 - try_except.py',
                  '50 - try_except_else_finally.py', '51 - debugando_com_pdb.py', '52 - modulo_random.py',
                  '53 - modulos_builtin.py', '54 - modulos_customizados.py', '55 - modulos_externos.py',
                  '56 - pacotes.py', '57 - dunder.py', '59 - leitura_de_arquivos.py', '59a - texto.txt',
                  '60 - seek_e_cursors.py', '61 - bloco_with.py', '62 - escrevendo_em_arquivos.py',
                  '63 - modos_abertura_arquivo.py','64 - stringIO.py', '65 - sistema_de_arquivos_navegacao.py',
                  '67 - entendendo_iterators_e_iteraveis.py', '68 - criando_sua_propria_versao_de_loop.py',
                  '69 - escrevendo_um_iterador_customizado.py', '70 - geradores.py',
                  '71 - teste_de_memoria_com_generators.py', '72 - teste_de_velocidade_com_expressoes_geradoras.py',
                  '73 - funcoes_de_maior_grandeza.py', '74 - o_que_sao_decoradores.py',
                  '75 - decoradores_com_diferentes_assinaturas.py', '76 - preservando_metadata_com_wraps.py',
                  '77 - forcando_tipos_de_dados_com_um_decorador.py', '78 - o_que_e_orientacao_a_objetos.py',
                  '79 - classes.py', '80 - atributos.py', '81 - metodos.py', '82 - objetos.py',
                  '83 - abstracao_e_encapsulamento.py', '84 - heranca.py', '85 - propriedades.py',
                  '86 - o_metodo_super.py', '87 - heranca_multipla.py', 'MRO.py', '89 - polimorfismo.py',
                  '90 - metodos_magicos.py', '300 - recolhendo_notas.py']
leitura_completa = [open(dado, 'r', encoding='UTF-8') for dado in lista_arquivos]
leitura_completa = [dado.read() for dado in leitura_completa]

with open('301 - todas_as_notas.txt', 'w', encoding='UTF-8') as notass:
    for i in range(0, len(leitura_completa)):
        notass.write(leitura_completa[i] +
                     '\n——————————————————————————————————————————————————————————————————————\n\n')
