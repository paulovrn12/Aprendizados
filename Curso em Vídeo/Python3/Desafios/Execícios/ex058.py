# Melhore o jogo do ex028.py onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# ex028:
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 ae 5
# e peça para o usuário tentar descorir qual foi o número escolhido pelo computador.

# 1. Quais são os dados de entrada necessários?
#   *

# 2. Que devo fazer com estes dados?
#   *

# 3. Quais são as restrições deste problema?
#   *

# 4. Qual é o resultado esperado?
#   *

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

from random import randint

escolha_pc = randint(0, 10)
acertou = False
tentativa = 0
while not acertou:
    escolha_user = int(input('Digite um valor entre 0 e 10: '))
    tentativa = tentativa + 1
    if escolha_user == escolha_pc:
        acertou = True
    else:
        if escolha_user < escolha_pc:
            print('Chute acima!')
        elif escolha_user > escolha_pc:
            print('Chute abaixo!')
print('Acertou com {} tentativas!'.format(tentativa))



