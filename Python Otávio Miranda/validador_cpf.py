# 1° - Receber o CPF como vier.
# 2° - Remover pontos, traços.
# 3° - Verificar se é possível converter em inteiro o CPF.
# 4° - Contar o número de dígitos do CPF.
# 5° - Separar dígitos em uma lista.
# 6° - Realizar o cálculo de validação do 1° dígito.
# 7° - Realizar o cálculo de validação do 2° dígito.
# 8° - Informar se o CPF é válido ou não.

# 7° - Regras para validação de CPF:
# CPF: ABC.DEF.GHI-JK

# SE A = B = C = D = E = F = G = H = I = J = K:
#   CPF NÃO VÁLIDO

# SE CPF = 123.456.789-12
#   CPF NÃO VÁLIDO

# PRIMEIRO DÍGITO (J):
# SOMA1 = (10*A) + (9*B) + (8*C) + (7*D) + (6*E) + (5*F) + (4*G) + (3*H) + (2*I)
# 11 - (SOMA1 % 11) = RESTO1
# SE RESTO1 > 10:
#   J = 0
# SENÃO:
#   J = RESTO1

# SEGUNDO DÍGITO (K):
# SOMA2 = (11*A) + (10*B) + (9*C) + (8*D) + (7*E) + (6*F) + (5*G) + (4*H) + (3*I) + (2*J)
# 11 - (SOMA2 % 11) = RESTO2
# K = RESTO2


class ValidadorCPF:
    def __init__(self, cpf):
        self._cpf = str(cpf)
        self._cpf.split()
        self._cpf = list(self._cpf)
        self._numeros = [] # [7, 0, 4, 1, 8, 9, 8, 8, 1, 4, 5]
        self._multip_dig10 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        self._multip_dig11 = [11, 10, 9, 8, 7, 6, 5, 4, 3]
        self._digitos = []
        self.resultados = [None, None, None, None, None]

    def numero_digitos(self):
        for _valor in self._cpf:
            if _valor.isnumeric():
                self._numeros.append(int(_valor))
            if len(self._numeros) != 11:
                print('numero_digitos False')
                return self.resultados[0] == False
            else:
                print('numero_digitos True')
                return self.resultados[0] == True

    def digitos_iguais(self):
        for e in range(0, len(self._numeros)):
            if self._numeros[e] == self._numeros[e + 1]:
                return self.resultados[1] == False
            else:
                return self.resultados[1] == True
        print(f'digitos_iguais: {self._numeros}')

    def digitos_sequenciais(self):
        if self._numeros == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]:
            print('digitos_sequenciais = False')
            return self.resultados[2] == False
        else:
            print('digitos_sequenciais = True')
            return self.resultados[2] == True

    def calculo_dig10(self):
        _produto = 1
        _soma = 0

        for c in range(0, 8):
            _produto = self._numeros[c] * self._multip_dig10[c]
            _soma += _produto
        _resto = 11 - (_soma % 11)
        if _resto > 10:
            self._multip_dig11[9] = 0
        else:
            self._multip_dig11[9] = _resto
        self._digitos[0] = self._multip_dig11[9]
        if self._digitos[0] != self._numeros[9]:
            print('calculo_dig10 False')
            return self.resultados[3] == False
        else:
            print('calculo_dig10 True')
            return self.resultados[3] == True

    def calculo_dig11(self):
        _produto = 1
        _soma = 0

        for c in range(0, 9):
            _produto = self._numeros[c] * self._multip_dig11[c]
            _soma += _produto
        _resto = 11 - (_soma % 11)
        self._digitos[1] = _resto
        if self._digitos[1] != self._numeros[10]:
            print('calculo_dig11 False')
            return self.resultados[4] == False
        else:
            print('calculo_dig11 True')
            return self.resultados[4] == True
