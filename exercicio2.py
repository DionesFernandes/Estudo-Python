"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_string = input('Digite a hora desejada: ')

try:
    hora_inteiro = int(hora_string)
    if hora_inteiro >= 0 and hora_inteiro <=11 :
        print(f'São exatamente {hora_inteiro} Horas, tenha um bom dia')

    elif hora_inteiro >= 12 and hora_inteiro <= 17:    
        print(f'São exatamente {hora_inteiro} Horas, Tenha uma boa tarde')

    elif hora_inteiro >=18 and hora_inteiro <= 23:
        print(f'São exatamente {hora_inteiro} Horas, Tenha uma boa noite')    
    
    else:
        print('Opção invalida!')

except:
     print('Não é número inteiro')    
