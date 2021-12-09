# ex061.py => Refaça o ex051.py, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos usando a estrutura while.
# Melhore o ex061.py perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

# 1. Quais são os dados de entrada necessários?
#   *

# 2. Que devo fazer com estes dados?
#   *

# 3. Quais são as restrições deste problema?
#   *

# 4. Qual é o resultado esperado?
#   *

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

primeiro = int(str(input('Digite o primeiro termo de uma P.A.: ')).strip())
razao = int(str(input('Digite a razão dessa P.A.: ')).strip())
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=', ')
        termo = termo + razao
        contador = contador + 1
    print('são os 10 primeiros termos dessa P.A.')
    mais = int(str(input('Quantos termos a mais deseja exibir? ')).strip())
print('P.A. com {} termos!'.format(total))