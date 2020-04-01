#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
#Seu programa deverá analisar se a 
#expressão está com os parenteses abertos ou fechados na ordem correta.
abriu = False
valida = True
contadorDeAberturas = 0
expressao = str(input('Digite uma expressão: '))
for cont, l in enumerate(expressao):
   if '(' in l :
    contadorDeAberturas =+1   ## Abriu um parenteses
   
   elif ')' in l:
    if contadorDeAberturas > 0:    # Verifica se não foi fechado sem abrir parenteses
       contadorDeAberturas =-1     # Fechou um parenteses
    else:
     valida = False
     break   

if valida == True and contadorDeAberturas == 0:  #Verifica se o passo anterior não apontou erro e,todos tem pares
  valida = True
else:
  valida = False

if valida == True:
    print ("Expressão valida!")
else:
    print('Expressão inválida!')     
