# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor será entregues.
# Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('''
╔════════════ PV BANK ════════════╗
║                                 ║
║ Cédulas disponíveis para saque: ║
║                                 ║
║   R$ 50,00           R$ 20,00   ║
║   R$ 10,00           R$  1,00   ║
╚═════════════════════════════════╝
''')
saque = int(input('Digite o valor que deseja sacar: R$ '))
montante = saque
ced = 50
totced = 0
while True:
    if montante >= ced:
        montante -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced},00')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if montante == 0:
            break