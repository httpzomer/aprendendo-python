user = str(input('Insira o usuário:\n'))
passw = str(input('Insira a senha:\n'))

while user == passw:
    print('O usuário não pode ser igual a senha.\n')
    user = str(input('Insira outro usuário:\n'))
    passw = str(input('Insira a senha:\n'))
print('Bem vindo!')
          
