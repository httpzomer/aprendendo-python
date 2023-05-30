nome = input('Nome: ')
item = input('O que colocar entre o nome: ')
tamanho = len(nome)
indice = 0
novo_nome = ''
while indice < tamanho:
    letra = nome[indice]
    novo_nome += f'{item}{letra}'
    indice+=1
print(novo_nome)
