import sys

# Generator expression, Iterables e Iterators em Python
# Generator é uma função que pausa
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

