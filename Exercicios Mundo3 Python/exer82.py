lista = []
listai = []
listap = []
while True:
        n = int(input('Digite um valor: '))
        lista.append(n)
        if n%2 == 0:
              listap.append(n)
        else:
              listai.append(n)
        r = str(input('Quer continuar [S/N]'))
        if r in 'nN':
            break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listap}')
print(f'A lista de impares é {listai}')
        