numeros =[]
while True:
    while True:
        num = int(input(("Inisira um numero: ")))
        if num in numeros:
            print('Numero invalido, já inserido anteriormente, tente novamente')
        else:
            break
    numeros.append(num)
    valida = input("Deseja continuar [S/N]: ")
    if(valida.lower() == 'n'):
        break
numeros.sort()
print(f'Os numeros digitados foram: {numeros}')