# 1. Quais são os dados de entrada necessários?
#   * um valor em reais do tipo int().

# 2. Que devo fazer com estes dados?
#   * calcular o menor número de cédulas possíveis para o valor de entrada do usuário.

# 3. Quais são as restrições deste problema?
#   * entrada ser um valor inteiro.
#   * entrada conter um valor entre 0 e 1,000,000.

# 4. Qual é o resultado esperado?
#   * ?
#   * ? nota(s) de R$ 100,00
#   * ? nota(s) de R$ 50,00
#   * ? nota(s) de R$ 20,00
#   * ? nota(s) de R$ 10,00
#   * ? nota(s) de R$ 5,00
#   * ? nota(s) de R$ 2,00
#   * ? nota(s) de R$ 1,00

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

valor = int(input())
nota_100 = valor // 100
nota_50 = valor % 100 // 50
nota_20 = valor % 100 % 50 // 20
nota_10 = valor % 100 % 50 % 20 // 10
nota_5 = valor % 100 % 50 % 20 % 10 // 5
nota_2 = valor % 100 % 50 % 20 % 10 % 5 // 2
nota_1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1
print("""{}
{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00""".format(valor, nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, nota_1))
