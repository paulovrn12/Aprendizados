# Crie um programa que faça o computador jogar Jokenpô com você.

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

from random import choice
from time import sleep

print("""
Olá, sou o seu PC e quero jogar Jokenpô contigo!
Escolha abaixo o número que representa sua escolha:
0 - pedra;
1 - papel;
2 - tesoura.
""")
escolhas = ['pedra', 'papel', 'tesoura']
escolha_user = int(str(input('Digite a sua escolha: ')).strip())
escolha_pc = choice(escolhas)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if escolha_user == escolha_pc:
    print('{}Deu empate! Ambos escolheram {}.{}'.format('\033[1;36', escolha_user, '\033[m'))
elif escolha_user == 0 and escolha_pc == escolhas[2]:
    print('{}Você ganhou! Pedra ganha de {}.{}'.format('\033[1;32m', escolha_pc, '\033[m'))
elif escolha_user == 0 and escolha_pc == escolhas[1]:
    print('{}Você perdeu! Pedra perde para {}.{}'.format('\033[1;31m', escolha_pc, '\033[m'))
elif escolha_user == 1 and escolha_pc == escolhas[0]:
    print('{}Você ganhou! Papel ganha de {}.{}'.format('\033[1;32m', escolha_pc, '\033[m'))
elif escolha_user == 1 and escolha_pc == escolhas[2]:
    print('{}Você perdeu! Papel perde para {}.{}'.format('\033[1;31m', escolha_pc, '\033[m'))
elif escolha_user == 2 and escolha_pc == escolhas[1]:
    print('{}Você ganhou! Tesoura ganha de {}.{}'.format('\033[1;32m', escolha_pc, '\033[m'))
elif escolha_user == 2 and escolha_pc == escolhas[0]:
    print('{}Você perdeu! Tesoura perde para {}.{}'.format('\033[1;31m', escolha_pc, '\033[m'))
