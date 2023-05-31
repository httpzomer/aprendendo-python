valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
soma = valor1+valor2
subtracao = valor1-valor2
multiplicacao = valor1*valor2
divisao = valor1/valor2
while True:
    sinal = str(input('+, -, * ou /\n'))

    if sinal == '+':
        print(f'Somando {valor1} + {valor2} = {soma}')
        valor1 = soma
        novoValor = float(input('Segundo valor: '))
        soma += novoValor
        print(novoValor)
    elif sinal == '-':
        print(f'Subtraindo {valor1} - {valor2} = {subtracao}')
    elif sinal == '*':
        print(f'Multiplicando {valor1} * {valor2} = {multiplicacao}')
    elif sinal == '/':
        print(f'Dividindo {valor1} / {valor2} = {divisao}')
          
