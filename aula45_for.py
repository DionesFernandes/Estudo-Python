"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter('Luiz') # __iter__() pode ser colocado dessas duas formas

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto
texto = 'Luiz' # iterável
# iteratador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:      # Os codigos acima é um exemplo de como o for funciona
    print(letra)        