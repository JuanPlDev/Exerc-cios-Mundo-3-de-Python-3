matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somac = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c]%2 == 0:
            soma += matriz[l][c]
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
scol = maior = 0
print(f'A soma dos pares é {soma}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol} ')
for c in range(0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2 linha é {maior}')
