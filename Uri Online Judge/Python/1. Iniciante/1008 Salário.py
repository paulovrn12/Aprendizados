# 1. Quais são os dados de entrada necessários?
#   * NUMBER, HOURS e VALUE

# 2. Que devo fazer com estes dados?
#   * SALARY = HOURS * VALUE

# 3. Quais são as restrições deste problema?
#   * dois números inteiros e um fracionário com duas casas decimais.

# 4. Qual é o resultado esperado?
#   * NUMBER = ##
#   * SALARY = U$ ######.##

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

NUMBER = int(input())
HOURS = int(input())
VALUE = float(input())
SALARY = HOURS * VALUE
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(NUMBER, SALARY))
