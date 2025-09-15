# OS COMANDOS IF-ELSE (CONDICIONAIS)

# CRIE UM PROGRAMA QUE RECEBA A NOTA DE UMA PESSOA. IMPRIMA "APROVADO(A)", NA TELA, CASO A NOTA SEJA MAIOR OU IGUAL A 7.0. CASO CONTRÁRIO, IMPRIMA "REPROVADO(A)", NA TELA

nota = float(input("Digite a sua nota: "))

if nota >= 7.0:
    print("Parabéns, você foi aprovado(a)!")
else:
    print("Que pena, você foi reprovado(a)!")