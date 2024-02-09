nome = 'Diones Fernandes'
altura = 1.86
peso = 92
imc = peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} Tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)