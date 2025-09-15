# CRIE UM PROGRAMA QUE PEÇA PARA QUE O USUÁRIO CONTINUE INFORMANDO NÚMEROS INTEIROS. O PROGRAMA DEVE ARMAZENAR TAIS NÚMEROS EM UMA LISTA. O PROGRAMA DEVE PARAR DE CAPTURAR NOVOS NÚMEROS CASO O USUÁRIO INSIRA 0 (ZERO). AO FINAL, O PROGRAMA DEVE INFORMAR A QUANTIDADE DE ELEMENTOS ADICIONADOS NA LISTA, BEM COMO O MENOR E O MAIOR ELEMENTOS DIGITADOS (EXCLUINDO O ZERO)

lista = []

while True:
    dado = int(input("Digite um número inteiro: "))
    if dado == 0:
        break
    lista.append(dado)
    

if len(lista) > 0:
    print(f"Quantidade de elementos adicionados: {len(lista)}")
    print(f"Menor número adicionado: {min(lista)}")
    print(f"Maior número adicionado: {max(lista)}")
else:
    print("Nenhum número foi digitado")