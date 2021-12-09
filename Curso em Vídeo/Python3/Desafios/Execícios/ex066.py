# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag, a condição de parada).

numeros = 0
soma = 0
contador = 0
# Repetição infinita:
while True:
    numeros =  int(str(input('Digite um número: ')).strip()) # Leitura de números interios no do usuário
    if numeros == 999: # se a entrada numérica do usuário for 999
        break # pause a repetição
    else: # senão
        soma += numeros # soma = soma + números (some os números em cada repetição)
        contador += 1 # contador = contador + 1 (conte o números digitados, ou o número de repetições)
print(f'Foram digitados {contador} e a soma dos mesmos é igual a {soma}!')
