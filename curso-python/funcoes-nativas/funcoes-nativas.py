# FUNÇÕES NATIVAS (BUILT IN FUNCTIONS)

# BIBLIOTECAS PADRÃO
# os
# sys
# math
# random
# datetime
# collections
# json

# FUNÇÕES NATIVAS
# abs() | abs() | any() | all()
# bool()
# chr() | callable()
# dir()
# enumerate() | eval() | exec()
# float() | filter()
# globals()
# help()
# int() | input() | id() | isinstance()
# len() | locals()
# max() | min() | map()
# open()
# print()
# range() | range()
# str() | sum() | sorted()
# type()
# zip()

# ==========================================

# CRIE UM CÓDIGO-FONTE QUE IMPORTE AS BIBLIOTECAS 'os' E 'math', E UTILIZE FUNÇÕES DESTAS BIBLIOTECAS PARA DEMONSTRAR SEU USO. 
# UTILIZE AO MENOS DUAS FUNÇÕES NATIVAS DO PYTHON, EM SEU CÓDIGO.

import math
import os

x = 16 
raiz_quad = math.sqrt(x)
print("Raiz quadrada de", x, "é igual a", raiz_quad)

angulo = 45
seno = math.sin(angulo)
print("O seno de", angulo, "é igual a", seno)

diretorio = os.getcwd()
print("O diretório corrente é", diretorio)

# os.system("cls") # FUNÇÃO QUE LIMPA A TELA

lista = [10, 20, 30]

tam = len(lista)
print("A lista", lista, "tem tamanho", tam)

soma = sum(lista)
print("A lista", lista, "tem um somatório igual a", soma)