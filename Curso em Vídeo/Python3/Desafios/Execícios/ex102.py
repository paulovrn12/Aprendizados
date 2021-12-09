# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    fator = numero
    if show:
        print(f'{numero}! = {numero} x ', end='')
    for c in range(numero-1, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print('1 = ',end='')
        fator = fator * c
    if show:
        print(fator)
    return fator

valor = int(str(input('Digite um valor: ')).strip())
respo = str(input('Deseja visualizar a fórmula do fatorial? [S/N]: ')).strip().upper()[0]
while respo not in 'SN':
        print('Digite apenas S para Sim e N para Não!')
        respo = str(input('Deseja visualizar a fórmula do fatorial? [S/N]: ')).strip().upper()[0]
if respo == 'S':
    print(fatorial(valor, show=True))
if respo == 'N':
    print(fatorial(valor, show=False))