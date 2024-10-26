from random import randint
from time import sleep
print('-='*8)
print('hora do jokenpô'.upper())
print('-='*8)
itens = ('pedra'.upper(),'papel'.upper(),'tesoura'.upper())
maq = randint(0,2)
print('Ok, vamos começar!'.upper())
print('''Escolha uma das opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
eu = int(input())
print('-='*8)
print('Eu escolho > {}'.format(itens[eu]))
print('-='*8)
print('A Maquina Escolheu...')
sleep(4)
print('{}'.format(itens[maq]))
print('-='*8)
if maq == 0:
    if eu ==0:
        print('-----empate-----'.upper())
    elif eu ==1:
        print('-----GANHEI-----')
    elif eu ==2:
        print('-----PERDI-----')
    else:
        print('Opção Inválida')
elif maq ==1:
    if eu ==0:
        print('-----PERDI-----')
    elif eu ==1:
        print('-----EMPATE-----')
    elif eu==2:
        print('-----GANHEI-----')
elif maq ==2:
    if eu ==0:
        print('-----GANHEI-----')
    elif eu ==1:
        print('-----PERDI-----')
    elif eu ==2:
        print('-----EMPATE-----')
print('~~'*15)
print('fim de jogo'.upper())

