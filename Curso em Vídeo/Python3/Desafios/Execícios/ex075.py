# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: usando tuplas.
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.


numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {numero}!')
print(f'a) O valor 9 foi digitado {numero.count(9)} vezes!')
if 3 in numero:
    print(f'b) O valor 3 apareceu na {numero.index(3)+1}ª posição!')
else:
    print('b) O valor 9 não foi digitado!')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')