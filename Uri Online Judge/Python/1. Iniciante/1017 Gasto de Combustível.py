# 1. Quais são os dados de entrada necessários?
#   * tempo gasto em horas sendo do tipo int().  (time_spent).
#   * velocidade média em km/h sendo do tipo int().  (average_speed).

# 2. Que devo fazer com estes dados?
#   * calcular a distancia percorrida em uma viagem.
#   * calcular e mostrar a quantidade de litros de combustível gastos nessa viagem.


# 3. Quais são as restrições deste problema?
#   * autonomia do veículo: 12km/l.  (autonomy).
#   * variavel no print com 3 casas decimais com o {:.3f}  (liters_needed).

# 4. Qual é o resultado esperado?
#   * ?.###

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

time_spent = int(input())
average_speed = int(input())
autonomy = 12
total_distance = time_spent * average_speed
liters_needed = total_distance / autonomy
print('{:.3f}'.format(liters_needed))
