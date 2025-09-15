# MATRIZES (LISTS MULTIDIMENSIONAIS)

# CRIE UMA LISTA DENOMINADA 'mat'. ADICIONE OUTRAS TRÊS SUB-LISTAS A 'mat'. CADA UMA DELAS COM OS RESPECTIVOS ELEMENTOS:
# 1- SUB-LISTA 1: 1, 2, 3
# 2- SUB-LISTA 2: 4, 5, 6
# 3- SUB-LISTA 3: 7, 8, 9
# IMPRIMA TODOS OS ELEMENTOS DA PRIMEIRA LINHA, UTILIZANDO 'mat', DENTRO DE UM LAÇO.
# IMPRIMA TODOS OS ELEMENTOS NUMÉRICOS ARMAZENADOS EM 'mat', UTILIZANDO LAÇOS.

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("ELementos da primeira linha: ")
for elem in mat[0]:
    print(elem, end=" ")

print()

print("Todos os elementos de mat: ")
for linha in mat:
    for elem in linha:
        print(elem, end=" ")
    print()


# ACESSANDO UM ELEMENTO NA MATRIZ
print("Penúltimo elemento da matriz: ", mat[2][1])