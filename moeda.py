def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)

def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)

def dobro(preco=0, formato=False):
    resultado = preco * 2
    return resultado if not formato else moeda(resultado)

def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if not formato else moeda(resultado)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print(f'Preço analisado: {moeda(preco)}') 
    print(f'{taxaa}% de aumento: {aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(preco, taxar, True)}')
    print('-'*30)