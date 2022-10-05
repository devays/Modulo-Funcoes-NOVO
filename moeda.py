def aumentar(valor = 0, porc = 0, set = True):
    res = valor + (valor * porc / 100)
    return valor if set is False else moeda(res)

def reduzir(valor = 0,porc = 0, set = True):
    res = valor - (valor * porc / 100)
    return valor if set is False else moeda(res)


def metade(valor = 0, set = True):
    metade = valor / 2
    return metade if set is False else moeda(metade)

def dobro(valor = 0, set = True):
    dobro = valor * 2
    return dobro if set is False else moeda(dobro)


def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor = 0, taxaa = 0, taxar = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)


    # Preço analisado:
    print(f'Preço analisado: \t{moeda(valor)}')

    # Dobro do preço: 
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    
    # Metade do preço:
    print(f'Metade do preço: \t{metade(valor, True)}')

    # # % de aumento: 
    print(f'{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}')

    # # % de redução:
    print(f'{taxar}% de aumento: \t{reduzir(valor, taxar, True)}')
