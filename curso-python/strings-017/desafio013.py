# DESENVOLVA UM PROGRAMA PARA TESTAR SUAS HABILIDADES COM STRINGS. CRIE UM PROGRAMA QUE CONTINUE PEDINDO PARA QUE O USUÁRIO INFORME VÁRIAS PALAVRAS. CONCATENE AS PALAVRAS DIGITADAS, SEPARANDO-AS POR ESPAÇOS. QUANDO O USUÁRIO DIGITAR '/exit', O PROGRAMA DEVE PARAR DE LER PALAVRAS (O '/exit' NÃO DEVE SER CONCATENADO). MOSTRE O RESULTADO DA CONCATENAÇÃO.

palavras = []

while True:
    palavra = input("Digite uma palavra (ou '/exit' para sair): ")
    if palavra == '/exit':
        break
    palavras.append(palavra)

resultado = " ".join(palavras)

print(f"\nResultado da concatenação:\n {resultado}")