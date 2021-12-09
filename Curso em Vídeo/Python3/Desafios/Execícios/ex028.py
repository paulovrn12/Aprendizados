# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 ae 5
# e peça para o usuário tentar descorir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro de 0 a 5.

# 2. Que devo fazer com estes dados?
#   * verificar se o número digitado pelo usuário coincide com o número randomizado pelo computador.

# 3. Quais são as restrições deste problema?
#   * uma entrada do tipo int() na faixa de 0 a 5.

# 4. Qual é o resultado esperado?
#   * mostrar ao usuário se ele acertou o número escolhido pelo computador.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * randomizar um número de 0 a 5 e armazená-lo em uma variavel escolha_pc.
#   * criar uma variavel1 escolha_user para armazenar o número escolido pelo usuário.
#   * mostrar se o valor escolhido pelo usuário coincide com o escolhido pela máquina.

from random import randint
from time import sleep

escolha_pc = randint(0, 5)
escolha_user = str(input('Digite um número de 0 a 5: ')).strip()
escolha_user = int(escolha_user)
print('CARREGANDO...')
sleep(3)
if escolha_user >= 0 and escolha_user <= 5:
    if escolha_pc == escolha_user:
        print('Parabéns, o número escolhido ({}) coincide com o número escolhido pelo PC!'.format(escolha_pc))
    else:
        print('Você errou, o número escolhido pelo PC foi o {}, não o {} escolhido por você!\nExecute o programa outra vez e tente acertar!'.format(escolha_pc, escolha_user))
else:
    print('Execute o programa novamente pois você deve escolher um número inteiro entre 0 e 5!')
