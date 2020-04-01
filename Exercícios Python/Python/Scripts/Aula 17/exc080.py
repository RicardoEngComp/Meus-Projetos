# Crie uma lista, que receba cinco valores, e, a cada valor inserido, a lista se auto ordene automáticamente, (sem utilizar o sort)

numeros = []
entrou = False
for c in range (0,5):
    num = int(input(f"insira o {c}° numero: "))
    if c == 0:
        numeros.append(num)
        print(f'Valor {num} adicionado ao indice {c} da lista')

    else:
        for cont in range (0,c):
            if num <= numeros[cont]:
                entrou = True
                numeros.insert(cont,num)
                print(f'Valor {num} adicionado ao indice {cont} da lista')
                break

        if entrou == False:
            numeros.insert(c,num)
            print(f'Valor {num} adicionado ao Final da lista')

print(numeros)
