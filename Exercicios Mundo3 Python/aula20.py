def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

#---------------------------------------------

# def dobra(lts):
#     pos = 0
#     while pos < len(lts):
#         lts[pos] *= 2
#         pos += 1

# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

#---------------------------------------------

# def contador(* núm):
#     for valor in núm:
#         print(f'{valor} ', end='')
#     print('FIM!')


# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
#-------------------------------------------

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)

# titulo(' CURSO EM VIDEO ')
# titulo(' PYTHON É MUITO BOM ')
# titulo('OI')

#--------------------------------------------

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')


# soma(b=4, a=5)
# soma(7, 2)