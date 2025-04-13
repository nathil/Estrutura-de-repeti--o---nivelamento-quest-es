# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
# conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber 
# um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo 
# operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor 
# em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o 
# programa deverá voltar ao ponto inicial, para registrar a próxima compra. 


valor = 1
total_compra = 0 

while valor != 0: 
    valor = float(input('Infome o valor da mercadoria:'))
    total_compra += valor

print(f'total da compra:{total_compra}')

dinheiro_fornecido = float(input('informe o dinheiro fornecido:'))
troco = dinheiro_fornecido - total_compra

print(f'troco:{troco:,.2f}')