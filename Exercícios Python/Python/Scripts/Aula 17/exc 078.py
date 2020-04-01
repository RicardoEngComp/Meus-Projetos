numeros = []
numerosOrdenados = []
for c in range (0,4):
    numeros.append(input(f'Digite um valor na posição {c}: '))

maior = numeros[0]
menor = numeros[0]

for c in numeros:
  if maior < c:
      maior = c

for c in numeros:
   if menor > c:
       menor = c
print(f'O maior numero é {maior} e aparece nas posicoes:', end= ' ' )
for c, l in enumerate(numeros):
    if maior in l:
        print(f'{c}...', end=' ')
print(" ")

print(f'O menor numero é {menor} e aparece nas posicoes:', end= ' ' )
for c, l in enumerate(numeros):
    if menor in l:
        print(f'{c}...', end=' ')
