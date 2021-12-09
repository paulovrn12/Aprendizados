# 1. Quais são os dados de entrada necessários?
#   * vendedor, salario, vendas

# 2. Que devo fazer com estes dados?
#   *  TOTAL = salario + (vendas * 0.15)

# 3. Quais são as restrições deste problema?
#   * vendas e salário e total em dinheiro com duas casas decimais

# 4. Qual é o resultado esperado?
#   *  TOTAL = R$ #####.##

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

vendedor = str(input())
salário = float(input())
vendas = float(input())
total = salário + (vendas * 0.15)
print('TOTAL = R$ {:.2f}'.format(total))
