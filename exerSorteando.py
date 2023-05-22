from random import choice
#
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo Aluno: '))
terceiro = str(input('Terceiro Aluno: '))
quarto = str(input('Quarto Aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
#
print('O aluno escolhido foi: {}'.format(choice(lista)))
