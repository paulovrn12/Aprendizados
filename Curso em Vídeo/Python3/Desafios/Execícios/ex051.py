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

p = int(input('Digite o primeiro termo de uma P.A.: '))
r = int(input('Digite a rasão de crescimento de uma P.A.: '))
for p in range(p, p+10*r, r):
    print(p, end= ', ')
print('fim da P.A.')
