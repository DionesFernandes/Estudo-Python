# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especifica (del)
# popitem - Apaga o útimo item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'Sobrenome': 'Miranda',
}



# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))  

# nome = p1.pop('nome')  - apagando item com a chave especificada
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()  - apagando a ultima chave adcionada no dicionário
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',  - atualiza o dicionário
#     'idade': 30,
# })

# p1.update(nome='novo valor', idade=30)  - outra forma de fazer o update

# tupla = (('nome', 'novo valor')('idade', 30))

lista = [['nome', 'novo valor'],['idade', 30]]
p1.update(lista)
print(p1)