# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Exemplo de resposta:
# Jogo #: [#, #, #, #, #, #]
# ...

from random import randint
jogos = []
numeros = []
n_jogos = int(input('\nDigite o número de jogos da MEGA que você deseja gerar: '))
print()
for n in range(0, n_jogos): 
    for c in range(0, 6):
        numeros.append(randint(1, 60))
    jogos.append(numeros[:])
    numeros.clear()
    print('Os jogos que você escolheu foram:')
    print(f'Jogo {n+1}:', end=' ')
    print(jogos[n])
    print()
