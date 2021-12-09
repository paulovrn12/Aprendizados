# Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma
# semelhante ao input() do Python, só que fazendo uma validação para aceitar apenas um valor numérico.
#Ex:
# n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): # se n.isnumeric() == True 
            valor = int(n)
            ok = True
        else:
	        print('Erro! Digite um número válido!')
        if ok:
            break
    return valor

num = leiaInt('Digite um número: ')
print(leiaInt(num))