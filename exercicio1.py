"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_string = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_string)
    if numero_inteiro % 2 == 0:
        print(f'Este número: { numero_inteiro } é par')
    else:    
        print(f'Este número: { numero_inteiro } é impar')

except:
     print('Não é número inteiro')    
