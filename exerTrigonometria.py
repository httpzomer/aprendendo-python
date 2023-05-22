import math
#
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}° tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f} '.format(angulo, seno, cosseno, tangente))
