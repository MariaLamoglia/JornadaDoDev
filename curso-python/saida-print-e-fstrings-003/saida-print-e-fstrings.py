# SAÍDA DE DADOS COM 'print()' E 'f-strings'

# CRIE UM PROGRAMA PARA PRATICAR O USO DO 'print()' JUNTO COM 'f-strings'. IMPRIMA, FORMATANDO, OS SEGUINTES DADOS:
# 10 (EM DECIMAL)
# 10 (DE DECIMAL, CONVERTIDO PARA BINÁRIO)
# 3.14159265 (COM TODAS AS CASAS DECIMAIS)
# 3.14159265 (COM 2 CASAS DECIMAIS)

print(f"O valor inteiro em decimal é: {10: d}")
print(f"O valor inteiro em binário é: {10: b}")

print(f"O valor de Pi é: {3.14159265: f}") # APARECEU "3.141593" PQ ELE ARREDONDOU, DADOS COM PONTOS FLUTUANTE (FLOAT) SÓ CONSEGUEM MANTER ATÉ 7 ALGARISMOS COM PRECISÃO
print(f"O valor de Pi com 2 casas decimais é: {3.14159265: .2f}")