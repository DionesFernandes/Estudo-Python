# Introdução às Generator Functions em Python
# generator = (n for n in range(1000))

def generator(n=0, maximum=10):
    while True:
        yield n   # a função yield pausa
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)