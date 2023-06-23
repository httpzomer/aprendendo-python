import random

cpf = ''    
limite1 = 10    #limite para o primeiro dígito
soma = 0        #soma para o primeiro dígito
novo_cpf = ''   #cpf com dígito
limite2 = 11    #limite para o segundo dígito
soma2 = 0       #soma para o segundo dígito

for x in range(0, 9):   #gera 9 números pro CPF 
    cpf += str(random.randint(0, 9))
    
#gera o primeiro digito:
    
for iteravel in cpf: 
    soma += int(iteravel)*limite1
    limite1 -= 1
    if limite1 == 1:
        break

if (soma*10)%11 > 9:
    novo_cpf = cpf+'0'
else:
    novo_cpf = cpf+str((soma*10)%11)
    
#gera o segundo dígito:
    
for iteravel2 in novo_cpf:
    soma2 += int(iteravel2)*limite2
    limite2 -= 1
    if limite2 == 1:
        break
    
if (soma2*10)%11 > 9:
    novo_cpf += '0'
else:
    novo_cpf += str((soma2*10)%11)
    
#fim
    
print(f'O CPF gerado é: {novo_cpf}')


