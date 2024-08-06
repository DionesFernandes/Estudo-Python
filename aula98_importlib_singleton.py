import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)  # reload ele recarrega o código inteiro do modulo, 
    print(i)                    # tudo que estive definido na aula98_m.py "isso não é comum".


print('Fim')