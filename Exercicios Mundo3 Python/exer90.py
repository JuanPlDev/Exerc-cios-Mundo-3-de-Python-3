situ = {} 
situ['nome'] = str(input('Nome: '))
situ['media'] = float(input('Média: '))
if situ['media'] > 7:
    situ['situação'] = 'Aprovado'
elif situ['media'] > 5 and situ['media'] < 7:
    situ['situação'] = 'Recuperação'
else:
    situ['situação'] = 'Reprovado'
print('-=' * 30)
# print(f'  -O nome é igual a {situ["nome"]}')
# print(f'  -Média é igual a {situ["media"]}')
# print(f'  -Situação é igual a {situ["situação"]}')
for k, v in situ.items():
    print(f'{k} é igual a {v}')
