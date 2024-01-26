valores = []
maior = 0
menor = 999
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    if v >= maior:
        maior = v
        pm = (c)
    if v <= menor:
        menor = v
        pme = (c)
print(f'O maior valor foi {maior}', end=' ')
print(f'na posição {pm} encontrei o maior valor')
print(f'O menor valor foi {menor}', end=' ')
print(f'na posição {pme} encontrei o menor valor')



    