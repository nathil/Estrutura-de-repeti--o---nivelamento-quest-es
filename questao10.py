# CALCULE E EXIBA A SOMA DE TODOSOS NÚMEROS PRIMOS DE 1 A 50.

soma_primo = 0 

# def e_primo(numero):
#     multiplos = 0
  
#     for i in range(2,numero):
#         if numero % i == 0: 
#             multiplos += 1
    
#     if multiplos == 0:
#         return True 
#     return False

#com função 

# for i in range (1,51): 
#     if i == 1: 
#         print('não é primo')
#     elif e_primo(i) == True:
#         soma_primo += i 
#     else: 
#         print(f'{e_primo(i)}[{i}]')
    

# print(soma_primo)


#sem função

for numero in range (1,51): #verifica todos os numero de 1 a 50
    multiplos = 0

    for i in range(2,numero): #verifica cada valor para ver se é primo
        if numero % i == 0: 
            multiplos += 1

    if numero == 1: 
        print('não é primo')
    
    elif multiplos == 0: #se for primo, então incrementamos 
        print(f'{True}[{numero}]') 
        soma_primo += numero
    else:
        print(f'{False}[{numero}]')

print(soma_primo) 