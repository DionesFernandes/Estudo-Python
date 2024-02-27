"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls') # cls = clear para limpar o terminal
        valor = input('valor: ') # Armanezando na variavel valor
        lista.append(valor) # método para anexar o objeto ao final da lista
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ') # indice que deseja apagar   

#                          --------- TRATAMENTO DE ERROS ------
        try:
            indice = int(indice_str) # Convertendo o valor recebido do input em int
            del lista[indice] 
        except ValueError: # tratando erro - Valor de argumento inadequado (do tipo correto)
            print('Por favor digite número int.')
        except IndexError: # tratando erro - índice de sequência fora do intervalo 
            print('ìndice não existe na lista') 
        except Exception: # tratando erro - erro desconhecido
            print('Erro desconhecido') 
#                         -----------------------------------------
            
    elif opcao == 'l': 
        os.system('cls')

        if len(lista) == 0: # função len retorna o número de itens em um contêiner (lista)
            print('Nada para listar')

        for i, valor in enumerate(lista): # retornando um objeto enumerado
            print(i, valor) # printando o indice e o valor
    else:
        print('Por favor, escolha i, a ou l.')        