# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.

clubes = ('Atlético-MG', 'Palmeiras' ,'Fortaleza', 'Flamengo', 'Bragantino',
          'Corinthians', 'Atlético-GO', 'Ceará SC', 'Athletico-PR', 'Internacional',
          'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia',
          'Fluminense', 'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')
ordem = sorted(clubes)

print(f'''
a) Os primeiros 5 primeiros colocados do Brasileirão 2021 no dia 23/05 são {clubes[0]}, {clubes[1]}, {clubes[2]}, {clubes[3]}, {clubes[4]}!

b) Os últimos 4 colocados do Brasileirão 2021 no dia 23/05 são {clubes[-4]}, {clubes[-3]}, {clubes[-2]}, {clubes[-1]}!

c) A lista dos times em ordem alfabética é: {ordem}!

d) O time do Chapecoense se encontra na {clubes.index('Chapecoense') + 1}ª posicão!
''')
# b) Os últimos 4 colocados do Brasileirão 2021 no dia 23/05 são {clubes[-4:]}