"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""
lista_a = ['luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()  # função copy copia o valor da variável lista_a e copia na lista_b

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)