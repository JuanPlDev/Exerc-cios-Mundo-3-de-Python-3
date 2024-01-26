Times = ('Palmeiras','cruzeiro','santos','bahia','fortaleza',
         'goias','botafogo','cuiaba','atletico mg','são paulo','vasco',
         'fluminense','bragantino','vitoia','sport','coritiba',
         'atletico pr','america mg','mirassol','corinthians')

print('Primeiros colocados')
for c in range(0,len(Times)):
    print(f'{c+1}° colocado {Times[c]}')
    if c ==4 :
        break
print('='*20)
print('Últimos colocados')
for c in range(16,len(Times)):
   print(f'{c+1}° colocado {Times[c]}')
print('='*20)
print(f'Times em ordem alfabética {sorted(Times)}')
print('='*20)
print(f'O time fluminense está na posição {Times.index("fluminense")}')