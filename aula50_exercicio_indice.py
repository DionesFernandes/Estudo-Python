"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')  # append, acrescenta o item 'João' a lista


indices = range(len(lista))  # foi usado range para gerar número e len para o tamanho da lista

for indice in indices:  # Foi usado o nome indice mas pode ser substituido pela letra "i"

    print(indice, lista[indice], type(lista[indice]))  # type me informa o tipo da lista