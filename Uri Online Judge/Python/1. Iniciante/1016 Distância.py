# 1. Quais são os dados de entrada necessários?
#   * uma distância em km sendo do tipo int().

# 2. Que devo fazer com estes dados?
#   * calcular quanto tempo em min leva para o carro Y tomar essa distancia do outro carro.

# 3. Quais são as restrições deste problema?
#   * Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com
# velocidade constante de 90 Km/h. Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja,
# consegue se afastar um quilômetro a cada 2 minutos.
#   * Fórmula: 1km * tempo decorrido = 2 min * distância percorrida. -----> tempo decorrido = 2 * distância percorrida.
#   * entrada do usuário: distancia percorrida.
#   * "variavel do problema": tempo decorrido.

# 4. Qual é o resultado esperado?
#   * ? minutos

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

travelled_distance = int(input())
elapsed_time = 2 * travelled_distance
print('{} minutos'.format(elapsed_time))
