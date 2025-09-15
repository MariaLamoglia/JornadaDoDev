# CRIE UM PROGRAMA QUE PEÇA PARA O USUÁRIO PREENCHER O CONTEÚDO DE UMA MATRIZ DE DIMENSÕES 3X4. APÓS INSERIDOS OS DADOS, REALIZE UMA BUSCA NA MATRIZ E INFORME QUAIS SÃO OS VALORES DAS LINHAS E COLUNAS (POSIÇÃO) DO MAIOR E DO MENOR ELEMENTO DE TODA A MATRIZ.

mat = []

print("Digite os valores para a matriz 3x4: ")

for i in range(3):
    linha = []
    for j in range(4):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    mat.append(linha)

maior = mat[0][0]
menor = mat[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(3):
    for j in range(4):
        if mat[i][j] > maior:
            maior = mat[i][j]
            pos_maior = (i, j)
        if mat[i][j] < menor:
            menor = mat[i][j]
            pos_menor = (i, j)

print(f"\nMaior elemento: {maior} na posição linha {pos_maior[0]}, coluna {pos_maior[1]}")
print(f"Menor elemento: {menor} na posição linha {pos_menor[0]}, coluna {pos_menor[1]}")