nome = str(input('Insira o nome\n'))
while len(nome) <= 3:
    nome = str(input('Insira um nome válido\n'))

    
idade = int(input('Quantos anos tem\n'))
while idade < 0 or idade > 150:
    idade = int(input('Insira uma idade válida\n'))

salario = float(input('Quanto você ganha?\n'))
while salario < 0:
    salario = float(input('Insira um valor válido\n'))

sexo = str(input('F ou M\n'))
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Insira um genêro válido\n'))


estado = str(input('Solteiro, Divorciado, Casado ou Viuvo\n'))
while estado != 'solteiro' and estado != 'divorciado' and estado != 'casado' and estado != 'viuvo':
    estado = str(input('Solteiro, Divorciado, Casado ou Viuvo\n'))   
    






