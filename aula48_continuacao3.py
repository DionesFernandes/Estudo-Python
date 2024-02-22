"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item ao índice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # nesse exemplo é feito uma concatenação das duas lista e apresentando o valor na lista "C"
lista_a.extend(lista_b) # nesse exemplo é feito uma extenssão da lista "A" junto com os valores da lista "B"
print(lista_a)