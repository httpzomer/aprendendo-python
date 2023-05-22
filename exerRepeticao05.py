A = int(input('Insira a quantidade de habitantes da menor cidade: '))
AA = float(input('Qual a porcentagem de crescimento?\n'))/100
B = int(input('Insira a quantidade de habitantes da cidade B: '))
BB = float(input('Qual a porcentagem de crescimento?\n'))/100
ano = 0

while A < B:
    A = A + (A*AA)
    B = B + (B*BB)
    ano = ano + 1
    print('cidade A: {:.2f}\ncidade B: {:.2f} passaram-se {} anos.'.format(A, B, ano))

