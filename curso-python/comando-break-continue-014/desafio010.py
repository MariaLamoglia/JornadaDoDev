# CRIE UM PROGRAMA QUE MOSTRE, NA TELA, UM CONTADOR. O CONTADOR DEVE SER INICIALIZADO COM ZERO. O USUÁRIO DEVE TER A OPÇÃO DE INCREMENTAR UMA UNIDADE AO CONTADOR, OU DE ENCERRAR O PROGRAMA. ENQUANTO O USUÁRIO CONTINUAR DECIDINDO INCREMENTAR O CONTADOR, O PROGRAMA NÃO DEVE SER ENCERRADO. O PROGRAMA ENCERRA SOMENTE QUANDO O USUÁRIO DECIDIR. UTILIZE UM LAÇO COM OS COMANDOS 'CONTINUE' E 'BREAK'.

contador = 0

while True:
    print(f"Contador atual: {contador}")
    escolha = input("Digite 'i' para incrementar uma unidade ao contador ou 's' para sair: ")

    if escolha == 'i':
        contador += 1
        continue
    elif escolha == 's':
        print("Encerrando contador...")
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue

