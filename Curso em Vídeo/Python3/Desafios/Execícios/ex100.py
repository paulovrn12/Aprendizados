# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostra a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

numeros = []
par = []

def sorteia(ini, fim):
    for c in range(0, 5):
        numeros.append(randint(ini, fim))
    print(f'Os números sorteados foram: ', end=' ')
    for n in range(0, 4):
        print(f'{numeros[n]},', end=' ')
    print('FIM!')    

def somaPar():
    for p in numeros:
        if p % 2 == 0:
            par.append[numeros]
    print(f'A soma dos valores pares da lista é igual a {sum(par)}!')


comeco = int(str(input('Sorteio de: ')).strip())
final = int(str(input('Até: ')).strip())

sorteia(comeco, final)

somaPar()
