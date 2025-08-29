# CRIE UM PROGRAMA QUE PEÇA AO USUÁRIO QUE INSIRA O SEU NOME, SEU TELEFONE E SEU NÚMERO DE IDENTIDADE. AO FINAL, IMPRIMA AS INFORMAÇÕES INFORMADAS PELO USUÁRIO.

nome = input("Digite o seu nome e sobrenome: ")
telefone = input("Digite o seu número de telefone:")
rg = input("Digite o seu número de identidade: ")

print(
    f"DADOS DO USUÁRIO:\n"
    f"Nome e Sobrenome: {nome}\n"
    f"Telefone: {telefone}\n"
    f"Número do RG: {rg}\n" 
)