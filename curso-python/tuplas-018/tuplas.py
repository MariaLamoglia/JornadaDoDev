# TUPLAS (TUPLES)

# DECLARE UMA TUPLA COM OS VALORES 0, 1, 3, 3, 5, 7, 7 E 7. IMPRIMA, NA TELA, O CONTEÚDO DA TUPLA, A QUANTIDADE DE ELEMENTOS E TAMBÉM QUANTOS ELEMENTOS IGUAIS A 7 ESTÃO NA TUPLA. IMPRIMA O ELEMENTO PRESENTE NA POSIÇÃO 4 NA TUPLA (QUINTA POSIÇÃO).

tupla = (0, 1, 3, 3, 5, 7, 7, 7)

print("Conteúdo da tupla: ", tupla)

qtde_elems = len(tupla)
print("Quantidade de elementos da tupla: ", qtde_elems)

qtde_setes = tupla.count(7)
print("Quantidade de elementos iguais a 7 na tupla: ", qtde_setes)

elem_pos_4 = tupla[4]
print("Elemento na posição 4 (quinta posição): ", elem_pos_4)