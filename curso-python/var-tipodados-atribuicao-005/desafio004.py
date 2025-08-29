# DECLARE QUATRO VARIÁVEIS, id(DO TIPO INTEIRO), nome(DO TIPO STRING), salario(DO TIPO FLOAT) E A VARIÁVEL brasileiro(DO TIPO BOOL)
# PEÇA PARA QUE O USUÁRIO INFORME OS DADOS ACIMA
# AO FINAL, IMPRIMA TUDO NA TELA UTILIZANDO f-strings

id = int(input("Digite o ID (número inteiro): "))
nome = input("Digite seu nome: ")
salario = float(input("Digite o seu salario (número decimal): "))
brasileiro = input("Você é brasileiro (sim/não)? ")

print(
    f"ID: {id}\n"
    f"Nome: {nome}\n"
    f"Salário: R$ {salario: .2f}\n"
    f"Brasileiro: {brasileiro}\n"
)