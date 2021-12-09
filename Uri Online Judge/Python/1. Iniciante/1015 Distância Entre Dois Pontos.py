# 1. Quais são os dados de entrada necessários?
#   * dois valores x1 e y2 em uma linha e dois valores x2 e y2 em outra linha, sendo todos do tipo float().

# 2. Que devo fazer com estes dados?
#   * calcular a distância entre eles sendo sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 3. Quais são as restrições deste problema?
#   * duas linhas contendo duas variaveis float() cada.
#   * uma saida com {:.4f}

# 4. Qual é o resultado esperado?
#   * ?.####

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

from math import sqrt
x1, y1 = str(input()).split(' ')
x2, y2 = str(input()).split(' ')
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('{:.4f}'.format(dist))
