# n1 = int(input('Digite o primeiro valor: '))
# n2 = int(input('Digite o segundo valor: '))
# n3 = int(input('Digite o terceiro valor: '))
# n4 = int(input('Digite o quarto valor: '))
t = (int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')),
     int(input('Digite o terceiro valor: ')),int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {t}')
print(f'O valor 9 aparece:{t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 foi digitado a primeira vez na posição {t.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('O valores pares digitados foram ', end='')
for n in t:
    if n%2 == 0:
        print(n, end=' ')