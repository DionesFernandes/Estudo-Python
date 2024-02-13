nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é  {nome}')
    print(f'Seu nome invertido é  {nome[::-1]}')
   
    count = 0
    for string in range(0, len(nome)):
        if nome[string] == " ":
            count += 1

    print(f"Seu nome contem { count } espaços")
    print(f"Seu nome tem { len(nome) - count } letras")
    print(f'Seu nome tem {len(nome)} caracteres totais')
    print(f'A primeira letra do seu nome', nome[0])
    print(f'A ultima letra do seu nome é {nome[-1]}' )
else:
    print('"Desculpa, você deixou campos vazios,"')    
