# Faça um programa que o faça jogar par ou ímpar com seu computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Raciocínio pessoal:
# Número par é aquele que é divisível por 2, tem como 0 o resto da divisão inteira por 2 (n % 2 == 0).
# Número ímpar é aquele que não é divisível por 2, tem como 1 o resto da divisão inteira por 2 (n % 2 != 0).
# Temos como variáveis as escolhas do pc e do usuário.
# Haverá um contador para contar o número de repetições, representando o número de vitórias consecutivas do usuário, que para de contar assim que ele perder.
# No início será necessário a importação de uma biblioteca que randomize números inteiros para representar a escolha do pc.
# Cenários comuns de jogo possíveis: 5
# 1 → se o usuário escolher ímpar e a soma der ímpar.
#   a contagem de vitórias consecutivas é realizada e o jogo continua pois o usuário ganha!
# 2 → se o usuário escolher par e a soma der par.
#   a contagem de vitórias consecutivas é realizada e o jogo continua pois o usuário ganha!
# 3 → se o usuário escolher ímpar e a soma der par.
#   a contagem de vitórias consecutivas para e o jogo para pois o usuário perde!
# 4 → se o usuário escolher par e a soma der ímpar.
#   a contagem de vitórias consecutivas para e o jogo para pois o usuário perde!
# 5 → soma_numeros = 0
#   empate, sem contágem de vitórias consecutivas e continua o jogo.


from random import randint

print('''
╔═════════ Par ou Ímpar ═════════╗
║                                ║
║ »»»»»»»»»»» REGRAS ««««««««««« ║
║                                ║
║  A seguir escolha primeiro um  ║
║    número de 0 a 5 dedos que   ║
║      deseja usar no jogo!      ║
║                                ║
║     E depois escolha entre:    ║
║        [I] para ÍMPAR          ║
║        [P] para PAR            ║
╚════════════════════════════════╝
''')

vitorias = 0 # contador de vitórias consecutivas do usuário.
while True: # enquanto o laço for verdadeiro ou não for parado, repita os comandos abaixo.
    escolha_user = str(input('Baseado nas REGRAS acima, você escolhe ímpar ou par? ')).strip().upper()[0] # escolha entre ímpar e par do usuário, sendo assim o pc dependente da escolha do usuário.
    numero_user = int(str(input('Digite um número de 0 a 5 dedos que deseja mostrar: ')).strip()) # representa o número de "dedos" colocados em jogo pelo usuário.
    if escolha_user in 'IP' and 0 <= numero_user <= 5: # se o usuário digitar I de Ímpar ou P de Par e o número escolhido por ele for entre 0 e 5.
        numero_pc = randint(0, 5) # representa o número de "dedos" colocados em jogo pelo pc.
        soma_numeros = 0 # soma dos "dedos" é zerada a cada jogo.
        soma_numeros = numero_user + numero_pc # soma dos "dedos".
        if escolha_user == 'I' and soma_numeros % 2 != 0: # se o usuário escolher ímpar e a soma der ímpar.
            print(f'Parabéns, você ganhou! O pc escolheu par e o número {numero_pc} e a soma deu {soma_numeros}!') # o usuário ganha.
            vitorias = vitorias + 1 # a contagem de vitórias consecutivas é realizada.
        if escolha_user == 'P' and soma_numeros % 2 == 0: # se o usuário escolher par e a soma der par.
            vitorias = vitorias + 1 # a contagem de vitórias consecutivas é realizada. 
            print(f'Parabéns, você ganhou! O pc escolheu ímpar e o número {numero_pc} e a soma deu {soma_numeros}!') # o usuário ganha.
        if escolha_user == 'I' and soma_numeros % 2 == 0: # se o usuário escolher ímpar e a soma der par.
            print('Você perdeu! Tente novamente.', end='') # o usuário perde.
            break # o laço e a contágem de vitórias é pausada.
        if escolha_user == 'P' and soma_numeros % 2 != 0: # se o usuário escolher par e a soma der ímpar.
            print('Você perdeu! Tente novamente.', end='') # o usuário perde.
            break # o laço e a contágem de vitórias é pausada.
        if soma_numeros == 0: # se ambos escolherem o número 0.
            print('Esse jogo deu empate! Tente novamente!', end='') # o jogo se empata.
    else: # se ele digitar qualquer coisa aleatória, que não seja I de Ímpar ou P de Par ou um número entre 0 e 5.
        print('Maluco(a), leia direito as regras no início do terminal!') # é repetido o laço com uma bronca pela falta de leitura.
print(f'Você teve {vitorias} consecutivas!') # exibição do número de vitórias consecutivas quando o usuário perder o jogo.
