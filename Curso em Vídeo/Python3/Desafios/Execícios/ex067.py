# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# Raciocínio pessoal:
# padrão de tabuada:
# X * Y = Z →  Y =  1   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  2   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  3   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  4   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  5   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  6   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  7   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  8   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y =  9   → X = entrada do usuário → Z = produto de X e Y
# X * Y = Z →  Y = 10   → X = entrada do usuário → Z = produto de X e Y
# Y vai de 1 até 10
# O ponto de parada é Y ir até 10
# Y é o contador de repetições somando 1 a cada repetição
while True:
    y = 0
    z = 0
    x = int(str(input('\nDigite um valor para mostrarmos a sua tabuada: ')).strip())
    if x < 0:
        print('''
        Fim da Tabuada''')
        break
    else: 
        print(f'''A seguir veremos a tabuada do {x}!
        ''')
        while True:
            if y == 10: # pode se usado um for ==> for c in range (1, 11)
                break
            else:
                y += 1
                z = x * y
                print(f'''║ {x}  * {y:2} = {z:2} ║''')
    
 