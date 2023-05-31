####Cria um loop e define as variáveis

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ') 

    numeros_validos = None

    num1_float = 0
    num2_float = 0
    
####Caso o tipo da variável não seja int/float retorna o while através do continue.
    
    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
####Retorna mensagem de erro até o operador for inserido de maneira correta.
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválidos.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
####Resolução dos cálculos
    
    print('O resultado é:')
    if operador == '+':
        print(f'{num1_float} + {num2_float}=',num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float}=',num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float}=',num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float}=',num1_float / num2_float)
        
####Quebra o while em caso de digitar a letra S na variável sair
        
    sair = input('Se quiser sair digite "s"\n').lower().startswith('s')

    if sair is True:
        break
