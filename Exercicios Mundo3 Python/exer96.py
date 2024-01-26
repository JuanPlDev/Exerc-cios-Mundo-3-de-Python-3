def area(larg, com):
    a = larg * com
    print(f'A area de um terreno de {larg}x{com} é de {a}m².')


print('CONTROLE DE TERRENOS')
print('=' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m)'))
area(l, c)