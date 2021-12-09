# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# leitura de dados e adição dos mesmos ao dicionário:
print()
campeonato = {}
campeonato['nome_player'] = str(input('Digite o nome do jogador: ')).strip()
campeonato['n_partidas'] = int(str(input('Digite o número de partidas jogadas: ')).strip())
campeonato['gols_total'] = 0
# calculo do total de gols: 
for n in range(1, campeonato['n_partidas'] + 1):
    campeonato[f'gols_partida{n}'] = int(str(input(f'Digite o número de gols da {n}ª partida: ')))
    campeonato['gols_total'] = campeonato['gols_total'] + campeonato[f'gols_partida{n}']
# exibição do nome, partidas e total de gols ao usuário:
print(f'''
Aproveitamento do jogador no campeonato:
-----------------------------------------
> Nome do jogador: {campeonato['nome_player']}.
> Partidas jogadas: {campeonato['n_partidas']}.
> Total de gols no campeonato: {campeonato['gols_total']}.
Sendo:''')
# exibição do aproveitamento do jogador (gols por partida):
n = 0
for key, value in campeonato.items():
    n = n + 1
    if key == f'gols_partida{n}':
        print(f'{value} gols na {n}ª partida!')
    else:
        continue
# exibição do dicionário completo: 
print(f'O dicionário completo é {campeonato}.')
    