# CRIE UM PROGRAMA QUE IMPRIMA, NA TELA, O NOME, A IDADE, O SALÁRIO E A NACIONALIDADE DE UMA PESSOA. VOCÊ IMPRIMIR TAIS DADOS UTILIZANDO FORMATAÇÃO POR MEIO DE F-STRINGS. UTILIZE CARACTERES DE ESCAPE PARA MELHOR ORGANIZAR SUA FORMATAÇÃO

nome = "Maria"
idade = "21"
salario = 2500.50
nacionalidade = "Brasileira"

print(
    f"Nome: {nome}\n"
    f"Idade: {idade} anos\n"
    f"Salário: R$ {salario: .2f}\n"
    f"Nacionalidade: {nacionalidade}"
)
