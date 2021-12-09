# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado
# não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)!')

jogador = str(input('Digite o nome de um jogador: ')).strip() # para que possa digitar valores vazios coloque 'str'
n_gols = str(input('Digite o número de gols desse jogador: ')).strip() # para que possa digitar valores vazios coloque 'str'
if n_gols.isnumeric(): # se a string n_gols for possível a conversão em número inteiro
    n_gols = int(n_gols) # converta para número inteiro.
else: # senão
    n_gols = 0
if jogador.strip() == '': # se o nome do jogador for uma string vazia
    ficha(gols=n_gols) # chame apenas gols na função
else: # senão
    ficha(jogador, n_gols) # chame todos os parâmetros