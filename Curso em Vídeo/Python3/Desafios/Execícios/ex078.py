# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


numeros = []
for c in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
print(f'A lista de números digitada foi {numeros}!')
print(f'''
O maior valor da lista é o {max(numeros)} que se encontra na {numeros.index(max(numeros))+1}ª posição!
O menor valor da lista é o {min(numeros)} que se encontra na {numeros.index(min(numeros))+1}ª posicão!
''')
