# COMANDOS IF-ELIF-ELSE (CONDICIONAIS)

# CRIE UM PROGRAMA QUE PEÇA PARA QUE O USUÁRIO INFORME UM NÚMERO INTEIRO COMPREENDIDO ENTRE 1 E 7.
# IMPRIMA "DOMINGO", CASO O NÚMERO SEJA 1;
# IMPRIMA "SEGUNDA-FEIRA", CASO O NÚMERO SEJA 2;
# IMPRIMA "TERÇA-FEIRA", CASO O NÚMERO SEJA 3 E ASSIM POR DIANTE;
# IMPRIMA "NÚMERO INVÁLIDO", CASO O NÚMERO NÃO ESTEJA COMPREENDIDO NO INTERVALO DE 1 A 7.

dia = int(input("Digite um número compreendido entre 1 e 7: "))

if dia == 1:
    print("Domingo!")
elif dia == 2:
    print("Segunda-feira!")
elif dia == 3:
    print("Terça-feira!")
elif dia == 4:
    print("Quarta-feira!")
elif dia == 5:
    print("Quinta-feira!")
elif dia == 6:
    print("Sexta-feira!")
elif dia == 7:
    print("Sábado!")
else:
    print("Número inválido!")