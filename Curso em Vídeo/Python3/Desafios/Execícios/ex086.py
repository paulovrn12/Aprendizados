# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores çidos pelo teclado.
#   ┌────┬────┬────┐
# 0 │    │    │    │
#   ├────┼────┼────┤
# 1 │    │    │    │
#   ├────┼────┼────┤
# 2 │    │    │    │
#   └────┴────┴────┘ 
# Y/X  0    1    2
# No final, mostre a matriz na tela, com a formatação correta.
# Exemplo de print de uma matriz:
# [Y, X] = n

# [0, 0] = 1
# [0, 1] = 2
# [0, 2] = 3

# [1, 0] = 4
# [1, 1] = 5
# [1, 2] = 6

# [2, 0] = 7
# [2, 1] = 8
# [2, 2] = 9
#
# [ 1 ][ 2 ][ 3 ]
# [ 4 ][ 5 ][ 6 ]
# [ 7 ][ 8 ][ 9 ]


print(f'''
 DISTRIBUIÇÃO DOS ELEMENTOS
 --------------------------
 ┌─ MODELO DE MATRIZ 3x3 ─┐
 │ ┌──────┬──────┬──────┐ │
 │ │[0, 0]│[0, 1]│[0, 2]│ │
 │ ├──────┼──────┼──────┤ │
 │ │[1, 0]│[1, 1]│[1, 2]│ │
 │ ├──────┼──────┼──────┤ │
 │ │[2, 0]│[2, 1]│[2, 2]│ │
 │ └──────┴──────┴──────┘ │
 └────────────────────────┘
''')
temp = [] # matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linhas = []
for y in range(0, 3): # for linha in range...
    for x in range(0, 3): # for coluna in range...
        temp.append(int(input(f'Digite um número para se o elemento [{y}, {x}]: '))) # para não precisar do uso de .append(), faça como mostrado acima. matriz[linha][coluna] = int(input('...'))
    linhas.append(temp[:]) # não necessário
    temp.clear() # não necessário
print(f'''
{linhas}

[ {linhas[0][0]} ][ {linhas[0][1]} ][ {linhas[0][2]} ]
[ {linhas[1][0]} ][ {linhas[1][1]} ][ {linhas[1][2]} ]
[ {linhas[2][0]} ][ {linhas[2][1]} ][ {linhas[2][2]} ]
''')

# Sujestão de print()
# 
# for linha in range(0, 3):
#   for coluna in range(0, 3):
#      print(f'[{matriz[linha][coluna]:^5}]', end='')
#   print()
