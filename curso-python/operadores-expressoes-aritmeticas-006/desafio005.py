# CRIE UM PROGRAMA QUE PEÇA AO USUÁRIO PARA INFORMAR TRÊS NÚMEROS COM CASAS DECIMAIS.
# CALCULE A MÉDIA ENTRE OS TRÊS NÚMEROS, E MOSTRE O RESULTADO NA TELA, FORMATADO PARA APRESENTAR APENAS DUAS CASAS DECIMAIS.

print("A seguir, você irá digitar apenas números com casas decimais!\n")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 2

print(f"A média obtida entre os três números é de: {media: .2f}")