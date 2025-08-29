# CRIE UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO DE 1 A 12. IMPRIMA, POR EXTENSO, O NOME DO RESPECTIVO MÊS DE ACORDO COM O CALENDÁRIO. POR EXEMPLO, SE O NÚMERO FOR 1, ENTÃO IMPRIMA "JANEIRO", NA TELA. IMPRIMA "MÊS INVÁLIDO", CASO O NÚMERO INFORMADO NÃO ESTEJA COMPREENDIDO ENTRE 1 E 12.

mes = int(input("Digite um número compreendido entre 1 e 12: "))

if mes == 1:
    print("Janeiro!")
elif mes == 2:
    print("Fevereiro!")
elif mes == 3:
    print("Março!")
elif mes == 4:
    print("Abril!")
elif mes == 5:
    print("Maio!")
elif mes == 6:
    print("Junho!")
elif mes == 7:
    print("Julho!")
elif mes == 8:
    print("Agosto!")
elif mes == 9:
    print("Setembro!")
elif mes == 10:
    print("Outubro!")
elif mes == 11:
    print("Novembro!")
elif mes == 12:
    print("Dezembro!")
else:
    print("Mês inválido!")