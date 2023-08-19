global total
total = 0
global limite_Saque
limite_Saque = 0

global extrato_Deposito
extrato_Deposito = []
global extrato_Saque
extrato_Saque = []

def deposito():
    global total
    global extrato_Deposito
    valor_Deposito = float(input())
    while valor_Deposito < 0 :
        valor_Deposito = float(input('Insira valores positivos:\n'))
    total += valor_Deposito
    extrato_Deposito.append(valor_Deposito)
    print(f'Você depositou R${valor_Deposito:.2f}\n')

def saque(x):
    global total
    global limite_Saque
    global extrato_Saque

    if limite_Saque == 3:
        print('Limite de saques atingidos. \n')
    else:
        if x > total:
            print('Você não possui saldo suficiente.\n')
        else:
            total -= x
            print(f'Você sacou R${x:.2f}, valor total na conta: R${total:.2f}\n')
            limite_Saque += 1
            extrato_Saque.append(x)

def extrato():
    for extratos_Deposito in extrato_Deposito:
        print(f'Você fez depósito de: R${extratos_Deposito:.2f}')
    print()
    for extratos_Saque in extrato_Saque:
        print(f'Você fez saque de: R${extratos_Saque:.2f}')
    

while True:
    print('[1] - Depositar \n[2] - Sacar \n[3] - Visualizar extrato \n[4] - Encerrar \n')
    acao = input('Qual das ações acima você gostaria de executar? \n')

    if acao == '1':
        print('Insira o valor a ser depositado:')
        deposito()
    elif acao == '2':
        asacar = float(input('Insira o valor que deseja sacar menor que o limite de R$500,00: \n'))
        while asacar > 500:
            asacar = float(input('Insira o valor que deseja sacar menor que o limite de R$500,00: \n'))
        saque(asacar)
    elif acao == '3':
        extrato()
    elif acao == '4':
        break
    else:
        print('Insira apenas as opções existentes.')