# 1. Quais são os dados de entrada necessários?
#   * raio

# 2. Que devo fazer com estes dados?
#   * area =  π * (raio ** 2)

# 3. Quais são as restrições deste problema?
#   * 

# 4. Qual é o resultado esperado?
#   *  A=#######.####

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

# area = π . raio**2
# π = 3.14159
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

raio = float(input())
π = 3.14159
area =  π * (raio ** 2)
print('A={:.4f}'.format(area))
