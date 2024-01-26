listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'lapizeira', 6.50,
            'regua', 4.20,
            'transferidor', 8,
            'estojo', 10,
            'canetas', 6.90,
            'bolsa', 50,
            'compasso', 8.50)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)