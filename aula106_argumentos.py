"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

#Definição da função

def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)


#Argumento posicional

soma(1, 2)  #  execução da função

#Argumento nomeado

soma(y=2, x=1)