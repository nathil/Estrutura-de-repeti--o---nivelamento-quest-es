valor1 = 12
valor2 = 3
valor3 = 6
valor4 = 4
valor5 = 2


for i in range(4):
    
    if valor1 > valor2: 
        valor1, valor2 = valor2, valor1
        
    if valor2 > valor3: 
        valor2, valor3 = valor3, valor2

    if valor3 > valor4: 
        valor3, valor4 = valor4, valor3

    if valor4 > valor5: 
        valor4, valor5 = valor5, valor4