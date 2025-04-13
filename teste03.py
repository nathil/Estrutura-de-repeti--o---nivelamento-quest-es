# Crie um programa que peça o salário e a idade de 10 pessoas. Ao final, mostre na tela: 
# A média das idades, a média dos salários

cont_idade = 0
cont_salario = 0


for i in range(10):
    idade = int(input('informe uma idade:'))
    salario = float(input('informe o seu salário:'))


    cont_idade += idade
    cont_salario += salario
    media_idade = cont_idade/10 
    media_salario = cont_salario/10

print(f'A média dos salários é de:{media_salario}\nA média das idades é de:{media_idade}')



