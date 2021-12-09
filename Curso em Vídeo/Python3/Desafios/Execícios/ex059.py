# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

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

nmb1 = int(str(input('Digite um número: ')).strip())
nmb2 = int(str(input('Digite outro valor: ')).strip())
menu = 0
while menu != 5:
    print('''
    ╔═════════ CALCULADORA ═════════╗
    ║                               ║
    ║──────────── MENU ─────────────║
    ║ [1] Soma dos números.         ║
    ║ [2] Produto dos números.      ║
    ║ [3] Maior dos números.        ║
    ║ [4] Nova entrada de números.  ║
    ║ [5] Fechar o programa.        ║
    ╚═══════════════════════════════╝
    ''')
    menu = int(str(input('Digite a acão que deseja realizar: ')))
    if menu == 1: # se o usuário escolher [1] Soma dos números.
        soma = nmb1 + nmb2
        print('A soma entre {} e {} é {}.'.format(nmb1, nmb2, soma))
    elif menu == 2: # se o usuário escolher [2] Produto dos números.
        prod = nmb1 * nmb2
        print('O produto de {} e {} é {}.'.format(nmb1, nmb2, prod))
    elif menu == 3: # se o usuário escolher [3] Maior dos números.
        if nmb1 > nmb2:
            maior = nmb1
        else:
            maior = nmb2
        print('Entre {} e {} o maior é {}.'.format(nmb1, nmb2, maior))
    elif menu == 4: # se o usuário escolher [4] Nova entrada de números.
        print('Informe outros dois números abaixo!')
        nmb1 = int(str(input('Digite um número: ')).strip())
        nmb2 = int(str(input('Digite outro valor: ')).strip())
    elif menu == 5: # se o usuário escolher [5] Fechar o programa.
        print('Fim a aplicação!')
    else:  # se o usuário digitar uma opção do menu não existente.
        print('Opção inválida, tente novamente!')