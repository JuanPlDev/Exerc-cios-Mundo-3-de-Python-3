# lanche = ('hamburgue', 'suco', 'pizza', 'pudim')
# print(lanche[-3:])
#tuplas sao imutaveis

lanche = ('hamburgue', 'suco', 'pizza', 'pudim','Batata frita')

for comida in lanche:
     print(f'Eu vou comer {comida}')


for pos, comida in enumerate(lanche):
     print(f'Eu vou comer {comida} na posição {pos}')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# print('Comi pra caramba')
    #  
# vai juntar as tuplas     
# a = (2,5,4)
# b = (5,8,1,2)
# c = a + b
# print(c)
#vai contar os 4
#print(c.count(4))
