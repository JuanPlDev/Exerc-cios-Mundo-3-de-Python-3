lista = []
while True:
        lista.append(int(input('Digite um valor: ')))
        r = str(input('Quer continuar [S/N]'))
        if r in 'nN':
            break
    
print(f'Voce digitou {len(lista)} elementos ')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecentes são {lista}')
if 5 in lista:
      print('O valor 5 foi encontra na lista')
else:
      print('O valor 5 não foi encontrado na lista')


        
