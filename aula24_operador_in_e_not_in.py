# Operadores in e not in
#String são iteráveis
#  0 1 2 3 4 5
#  d i o n e s
# -6-5-4-3-2-1
# nome = 'diones'
# print(nome[2])
# print(nome[-4])

# print('nes' in nome)
# print('zero' in nome)
# print(18 * '-')
# print('nes' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')    