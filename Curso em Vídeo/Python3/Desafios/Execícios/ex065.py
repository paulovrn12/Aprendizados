# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.

resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'S':
    num = int(str(input('Digite um valor para adicionarmos a média: ')))
    soma = soma + num
    quant = quant + 1
    resp = str(input('Quer continuar? [S/N]: ').upper().strip())[0]
    if quant ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('A média dos {} termos somados é igual a {}, sendo {} o maior e {} o menor valor!'.format(quant, media, maior, menor))
