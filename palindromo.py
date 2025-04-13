#palindromo

palavra = input('insira uma palavra:')

palavra_invertida = ''

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

if palavra_invertida == palavra:
    print('É um palindromo')
else:
    print('Não é um palindromo')