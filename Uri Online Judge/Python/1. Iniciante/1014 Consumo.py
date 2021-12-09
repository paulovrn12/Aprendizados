# 1. Quais são os dados de entrada necessários?
#   * X sendo int() representando a distância total percorrida em km.
#   * Y sendo float() representando o total de combustível gasto com {:.1f} em l.

# 2. Que devo fazer com estes dados?
#   * calcular o consumo médio de um automóvel.

# 3. Quais são as restrições deste problema?
#   * uma entrada X sendo int() e outra entrada Y sendo float().
#   * uma saída sendo com {:.3f}.

# 4. Qual é o resultado esperado?
#   * ?.### km/l

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

X = int(input())
Y = float(input())
M = X / Y
print('{:.3f} km/l'.format(M))
