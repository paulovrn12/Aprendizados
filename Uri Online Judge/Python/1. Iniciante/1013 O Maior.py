# 1. Quais são os dados de entrada necessários?
#   * leitura de três valores inteiros a, b, c.

# 2. Que devo fazer com estes dados?
#   * calcular qual é o valor maior usando: MaiorAB = (a + b + abs(a - b)) / 2

# 3. Quais são as restrições deste problema?
#   * a fórmula calcula apenas 2 valores, deve ser feito mais um passo na verificação.

# 4. Qual é o resultado esperado?
#   * ? eh o maior

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

a, b, c = str(input()).split(' ')
a = int(a)
b = int(b)
c = int(c)
MaiorAB = int((a + b + abs(a - b)) / 2)
if a > b:
    MaiorAC = int((a + c + abs(a - c)) / 2)
    print('{} eh o maior'.format(MaiorAC))
else:
    MaiorBC = int((b + c + abs(b - c)) / 2) 
    print('{} eh o maior'.format(MaiorBC))
