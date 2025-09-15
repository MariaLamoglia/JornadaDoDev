# COMANDO IF (CONDICIONAIS)

# CRIE UM PROGRAMA QU PEÇA PARA QUE O USUÁRIO INFORME O VALOR DE SUA NOTA. CASO A NOTA SEJA MAIOR OU IGUAL A 7.O, ENTÃO IMPRIMA "APROVADO(A)", NA TELA.

nota = float(input("Digite a nota: "))

if nota >= 7.0:
    print("Parabéns, você foi aprovado(a)!")

# CRIE UM PROGRAMA QUE PEÇA PARA QUE O USUÁRIO INFORME O VALOR DE SUA NOTA. CASO A NOTA INFORMADA SEJA MENOR QUE 7.0 MAS SIMULTANEAMENTE MAIOR OU IGUAL A 4.0, ENTÃO IMPRIMIR "TEM DIREITO A EXAME!"

nota2 = float(input("Digite a sua nota: "))

if nota2 >= 7.0:
    print("Parabéns, você foi aprovado(a)!")
if nota2 < 7.0 and nota2 >= 4.0:
    print("Recuperação! Você tem direito a exame.")