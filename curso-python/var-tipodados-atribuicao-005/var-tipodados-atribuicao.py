# VARIÁVEIS, TIPOS DE DADOS E ATRIBUIÇÃO

# CRIE UM PROGRAMA PARA PRATICAR O USO DE VARIÁVEIS COM ENTRADA E SAÍDA DE DADOS. DECLARE TRÊS VARIÁVEIS, idade = 0, altura = 0 E nome=""
# PEÇA PARA QUE O USUÁRIO INFORME A IDADE, ALTURA E NOME DE UMA PESSOA, E ARMAZENE NAS RESPECTIVAS VARIÁVEIS, MANTENDO SEUS TIPOS DE DADOS CONFORME O ESTABELECIDO DURANTE A DECLARAÇÃO DELAS.
# AO FINAL, OS DADOS INFORMADOS NA TELA.

idade = 0
altura = 0.0
nome = ""

idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
nome = input("Digite o seu nome: ")

print("Idade digitada: ", idade)
print("Altura digitada: ", altura)
print("Nome digitado: ", nome)