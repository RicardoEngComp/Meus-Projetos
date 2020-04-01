palavras = ('camelo','medalha','dorminhoco','sanfona','putaria','escola','malandro','caminhao')

for p in palavras:
    print(f'Na palavra {p} temos:', end = '')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end = ' ')

    print('')