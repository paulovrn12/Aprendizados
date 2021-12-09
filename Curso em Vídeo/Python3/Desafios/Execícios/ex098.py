# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e relize a contagem.
# Seu programa tem que realizar três contagens através da função criada.
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.

def contador(inicio, fim, passo):
    # para uma contagem crescente correta:
    if inicio < fim and passo > 0: # passo positivo.
        for c in range (inicio, fim + 1, passo):
            print(c, end=', ')
        print('FIM!')
    # para uma contagem crescente corrigida:
    if inicio < fim and passo < 0: # passo negativo.
        passo = passo * -1
        for c in range (inicio, fim + 1, passo):
            print(c, end=', ')
        print('FIM!') 
    # para uma contagem decrescente correta:
    if inicio > fim and passo < 0: # passo negativo.
        for c in range (inicio, fim - 1, passo):
            print(c, end=', ')
        print('FIM!')
    # para uma contagem decrescente corrigida:
    if inicio > fim and passo > 0: # passo positivo.
        passo = passo * -1
        for c in range (inicio, fim - 1, passo):
            print(c, end=', ')
        print('FIM!')
    # início igual a fim:
    if inicio == fim:
        print(f'{inicio}, FIM!')
    # passo igual a zero.
    if passo == 0:
      print('O passo não pode ser igual a ZERO!')  

comeco = int(str(input('Digite o um valor de começo: ')).strip())
termino = int(str(input('Digite um valor de término: ')).strip())
passar = int(str(input('Digite um valor de passo: ')).strip())

print('a) De 1 até 10, de 1 em 1:')
contador(1, 10, 1)

print('b) De 10 até 0, de 2 em 2:')
contador(10, 0, -2)

print('c) Uma contagem personalizada:')
contador(comeco, termino, passar)



















