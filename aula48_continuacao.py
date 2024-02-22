"""
Listas em python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)    
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # Deleta o indice 2 da lista
# print(lista)
# print(lista[2]) # Lista atualizada depois de ter deletado o indice 2 

lista.append(50) # append acrescenta mais 1 indice na lista
lista.pop() # pop exclui o ultimo indice quando ele é declarado
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # foi criado uma variável para mostrar a função pop, excluindo o último índice
print(lista, 'Removido,', ultimo_valor)
# 

""" Em listas grandes não se usa esse método pois fará com que o processamento fique lento,
porque o python atualizará todos os indices"""