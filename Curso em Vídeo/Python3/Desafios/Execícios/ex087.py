# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha. 

# Exemplo de print de uma matriz:
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
#   ┌────┬────┬────┐
# 0 │    │    │    │
#   ├────┼────┼────┤
# 1 │    │    │    │
#   ├────┼────┼────┤
# 2 │    │    │    │
#   └────┴────┴────┘ 
# Y/X  0    1    2
#
#  [ 1 ][ 2 ][ 3 ]
#  [ 4 ][ 5 ][ 6 ]
#  [ 7 ][ 8 ][ 9 ]
#
# A soma dos valores pares é 20.
# A soma dos valores da terceira coluna é 18.
# O maior valor da segunda linha é 6.

# [Y, X] = n

print(f'''
 DISTRIBUIÇÃO DOS ELEMENTOS
 --------------------------
 ┌─ MODELO DA MATRIZ 3x3 ─┐
 │ ┌──────┬──────┬──────┐ │
 │ │[0, 0]│[0, 1]│[0, 2]│ │
 │ ├──────┼──────┼──────┤ │
 │ │[1, 0]│[1, 1]│[1, 2]│ │
 │ ├──────┼──────┼──────┤ │
 │ │[2, 0]│[2, 1]│[2, 2]│ │
 │ └──────┴──────┴──────┘ │
 └────────────────────────┘
''')
temp = []
linhas = []
pares = []
linha2 = []
coluna3 = []
for y in range(0, 3): # [#, ]
    for x in range(0, 3): # [, #]
        temp.append(int(input(f'Digite um número para se o elemento [{y}, {x}]: ')))
        if temp[-1] % 2 == 0:
            pares.append(temp[-1])
        if x == 2:
            coluna3.append(temp[-1])
    if y == 1:
        linha2.append(temp[:])
    linhas.append(temp[:])
    temp.clear()
print(f'''
[ {linhas[0][0]} ][ {linhas[0][1]} ][ {linhas[0][2]} ]
[ {linhas[1][0]} ][ {linhas[1][1]} ][ {linhas[1][2]} ]
[ {linhas[2][0]} ][ {linhas[2][1]} ][ {linhas[2][2]} ]


a) A soma dos valores pares digitados é {sum(pares)} sendo seus itens {pares}!
b) A soma dos valores da terceira coluna é {sum(coluna3)} sendo seus itens {coluna3}!
c) O maior valor da segunda linha é {max(linha2[0])} sendo seus itens {linha2[0]}!
''')

