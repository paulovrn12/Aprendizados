# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
# As listas de pares e ímpares devem estar dentro de outra lista de números.

temp = []
numeros = [] # ou numeros [[], []] sendo numeros[0] pares e numeros [1] ímpares.
pares = []
impares = []

for c in range(1, 8):
    temp.append(int(input(f'Digite o {c}º número inteiro: ')))
    if temp[0] % 2 == 0:
        pares.append(temp[0]) # numeros[0].append()
    elif temp[0] % 2 == 1: # temp[1]...
        impares.append(temp[0]) # numeros[1].append()
    temp.clear()
numeros.append(pares[:]) # eliminando essa linha até...
numeros.append(impares[:]) # ...
pares.clear() # ...
impares.clear() # essa linha.
numeros[0].sort()
numeros[1].sort()
print(f'''
A lista de números digitada é {numeros}!
Sendo os números pares {numeros[0]} e os ímpares {numeros[1]}.
''')
