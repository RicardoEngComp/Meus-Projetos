numeros = ((int(input('Digite um numero:'))),
           (int(input("Digite um numero:"))),
           (int(input("Digite um numero:"))),
           (int(input("Digite um numero:"))))
print (f'Você digitou os numeros:{numeros}')

print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 03 apareceu na posicão:{numeros.index(3)+1}')
else:
    print('O valor 03 não foi inserido')
print('Os valores pares são:', end =' ')
for n in numeros:
    if n % 2 == 0:
       print( n, end=' ')



