from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        cont += 1
        if valor > maior:
            maior = valor
    print(f'Foram informado {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}')
    

    


maior(2,5,9,2,3,1)
maior(1,0,5,9,12)
maior(6,3)
maior(8,10,1)
maior(6)
maior()
