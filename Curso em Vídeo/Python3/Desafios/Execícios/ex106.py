# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar um comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.

def ajuda(função):
    print(help(função))

leitura = str(input('Digite uma função do python: '))

ajuda(leitura)