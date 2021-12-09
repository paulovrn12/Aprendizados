# 1. Quais são os dados de entrada necessários?
#   * uma idade em dias de uma pessoa do tipo int().

# 2. Que devo fazer com estes dados?
#   * converter dias no formato ano, mês e dia.

# 3. Quais são as restrições deste problema?
#   * considere que um (1) ano tem 365 dias.
#3  * considere que um (1) mês tem 30 dias.

# 4. Qual é o resultado esperado?
#   * ? ano(s)
#   * ? mes(es)
#   * ? dia(s)

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

number = int(input())
n_ano = number // 365
n_mes = number % 365 // 30
n_dia = number % 365 % 30
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(n_ano, n_mes, n_dia))
