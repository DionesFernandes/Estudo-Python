# Generator expression, Iterables e Iterators em Python

# iterables tem a responsabilidade de deter os valores sequêncialmente
iterable = ['Eu', 'Tenho', '__iter__'] 

# iterator tem a única responsabilidade de entregar um valor por vez
iterator = iter(iterable) # tem __iter__ e __next__