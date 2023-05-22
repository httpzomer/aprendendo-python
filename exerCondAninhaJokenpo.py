import random
print('{:=^40}'.format(' JO KEN PO '))
      
cpu = random.choice(['pedra', 'papel', 'tesoura'])
u = str(input('FAÇA SUA ESCOLHA:\n- Pedra\n- Papel\n- Tesoura\n')).lower()

if u == 'pedra' and cpu == 'pedra':
    print('Empate, você escolheu {} e o adversário {}.'.format(u, cpu))
elif u == 'papel' and cpu == 'papel':
    print('Empate, você escolheu {} e o adversário {}.'.format(u, cpu))
elif u == 'tesoura' and cpu == 'tesoura':
    print('Empate, você escolheu {} e o adversário {}.'.format(u, cpu))
elif u == 'pedra' and cpu == 'papel':
    print('Você perdeu, ele escolheu {} e você {}.'.format(cpu, u))
elif u == 'pedra' and cpu == 'tesoura':
    print('Você ganhou, ele escolheu {} e você {}.'.format(cpu, u))
elif u == 'papel' and cpu == 'pedra':
    print('Você ganhou, ele escolheu {} e você {}.'.format(cpu, u))
elif u == 'papel' and cpu == 'tesoura':
    print('Você perdeu, ele escolheu {} e você {}.'.format(cpu, u))
elif u == 'tesoura' and cpu == 'pedra':
    print('Você perdeu, ele escolheu {} e você {}.'.format(cpu, u))
elif u == 'tesoura' and cpu == 'papel':
    print('Você ganhou, ele escolheu {} e você {}.'.format(cpu, u))
