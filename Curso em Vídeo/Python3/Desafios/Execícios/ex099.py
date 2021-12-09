# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.

def maior(* num):
    print(max(num[0]))

numeros = []
while True:
    numero = int(str(input('Digite um número inteiro: ')).strip())
    numeros.append(numero)
    continuar = str(input('Deseja adicionar mais números? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Digite apenas S para Sim e N para Não!')
        continuar = str(input('Deseja adicionar mais números? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('O maior números é', end=' ')
maior(numeros)
