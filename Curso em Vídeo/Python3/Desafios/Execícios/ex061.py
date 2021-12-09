# Refaça o ex051.py, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos usando a estrutura while.

# ex051.py
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os dez primeiros termos dessa progressão.

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
razao_pa = int(str(input('Digite a razão dessa P.A.: ')).strip())
n_termos = 1 # contador
termos = primeiro
while n_termos <= 10:
    print('{}'.format(termos), end=', ')
    termos = termos + razao_pa
    n_termos = n_termos + 1
print('são os 10 primeiros termos dessa P.A.')

    
