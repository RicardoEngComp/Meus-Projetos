produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 20,
            'Transferidor', 4.20,
            'Compasso',9.99)
print('-'*30)
print('TABELA DE PREÇOS')
print('-'*30)


for pos in range(0,len(produtos)):
    if pos % 2 ==0:
        print(f'{produtos[pos]:.<30}', end ='')
    else:
        print(f' R$ {produtos[pos]:>5.2f}')