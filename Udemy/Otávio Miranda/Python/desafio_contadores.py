from time import sleep

def contador_for_normal():
    for c in range(0, 11):
        print(c)
        sleep(1)
    print('FIM!')

def contador_for_regressivo():
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('FIM!')

def contador_while_normal():
    c = -1
    while c != 10:
        c += 1
        print(c)
        sleep(1)
    print('FIM!')

def contador_while_regressivo():
    c = 11
    while c != 0:
        c -= 1
        print(c)
        sleep(1)
    print('FIM!')

contador_while_regressivo()