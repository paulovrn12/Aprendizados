# 1. Quais são os dados de entrada necessários?
#   * um valor de reais N do tipo float().

# 2. Que devo fazer com estes dados?
#   * converter no formato de cédulas e moedas.

# 3. Quais são as restrições deste problema?
#   * entrada em float().

# 4. Qual é o resultado esperado?
#   * NOTAS:
#   * ? nota(s) de R$ ###.##
#   * ...
#   * MOEDAS:
#   * ? moeda(s) de R$ #.##
#   * ...

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

N = float(input())
C_100 = N // 100
C_50 = N % 100 // 50
C_20 = N % 100 % 50 // 20
C_10 = N % 100 % 50 % 20 // 10
C_5 = N % 100 % 50 % 20 % 10 // 5
C_2 = N % 100 % 50 % 20 % 10 % 5 // 2
M_1 = N % 100 % 50 % 20 % 10 % 5 % 2 // 1
M_50 = N % 100 % 50 % 20 % 10 % 5 % 2 % 1 // 0.5
M_25 = N % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 // 0.2
M_10 = N % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 // 0.1
M_05 = N % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 % 0.1 // 0.05
M_01 = N % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 // 0.01
print("""NOTAS:
{:.0f} nota(s) de R$ 100.00
{:.0f} nota(s) de R$ 50.00
{:.0f} nota(s) de R$ 20.00
{:.0f} nota(s) de R$ 10.00
{:.0f} nota(s) de R$ 5.00
{:.0f} nota(s) de R$ 2.00
MOEDAS:
{:.0f} nota(s) de R$ 1.00
{:.0f} nota(s) de R$ 0.50
{:.0f} nota(s) de R$ 0.25
{:.0f} nota(s) de R$ 0.10
{:.0f} nota(s) de R$ 0.05
{:.0f} nota(s) de R$ 0.01""".format(C_100, C_50, C_20, C_10, C_5, C_2, M_1, M_50, M_25, M_10, M_05, M_05, M_01))
