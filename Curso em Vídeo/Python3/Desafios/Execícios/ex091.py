# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

resultados = {}
for c in range(0, 4):
    resultados[f'jogador{c+1}'] = randint(1, 6)
'''for key, value in resultados.items():
    print(f'O {key} jogou {value}')'''

for i in sorted(resultados, key = resultados.get, reverse=True): # copiado (não compriendi)
    print(f'O {i} jogou {resultados[i]}')