# CRIE UM PROGRAMA QUE RECEBA O NOME E A IDADE DE UMA PESSOA. CASO A IDADE SEJA MAIOR OU IGUAL A 18, IMPRIMIR O NOME DA PESSOA E INFORMAR, NA TELA, QUE ELA É MAIOR DE IDADE. CASO CONTRÁRIO, NÃO IMPRIMIR O NOME E INFORMAR QUE A PESSOA É MENOR DE IDADE.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Nome:", nome)
    print("Idade:", idade)
    print("Você é maior de idade!")
else:
    print("idade:", idade)
    print("Você é menor de idade!")