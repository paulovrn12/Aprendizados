# 1. Quais são os dados de entrada necessários?
#   * duração de tempo em segundos.  (N).

# 2. Que devo fazer com estes dados?
#   * converter N no formato hora:minuto:segundo.

# 3. Quais são as restrições deste problema?
#   * uma entrada do tipo int().

# 4. Qual é o resultado esperado?
#   * ##:##:##

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

N = int(input())
H = N // 3600
M = N % 3600 // 60
S = N % 3600 % 60  
print('{}:{}:{}'.format(H, M, S))
