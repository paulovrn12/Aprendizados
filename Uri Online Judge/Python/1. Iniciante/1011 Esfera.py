# 1. Quais são os dados de entrada necessários?
#   * raio R de uma esfera em float().

# 2. Que devo fazer com estes dados?
#   * VOLUME = (4/3.0) * pi * R ** 3
#   * pi = 3.14159

# 3. Quais são as restrições deste problema?
#   * resultado com três casas decimais.

# 4. Qual é o resultado esperado?
#   * VOLUME = ?.###

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1011

R = float(input())
pi = 3.14159
VOLUME = (4 / 3.0) * pi * R ** 3
print('VOLUME = {:.3f}'.format(VOLUME))
