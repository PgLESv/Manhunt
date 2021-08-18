import random
import os

jogadores = []
num_to_select = 2
num_to_select3 = 3

print('ALEATORIZADOR DE TIMES DO MANHUNT')

quantidade = int(input('Insira quantos jogadores irão jogar: '))

if quantidade <= 1:
    print ('Não tem como jogar com uma pessoa!')
    os.system("pause")

elif quantidade == 2:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)

    runner = random.choice(jogadores)
    print(f'O runner é {runner}')
    os.system("pause")

elif quantidade == 3:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)
    jogadores.append(player3)

    runner = random.choice(jogadores)

    print(f'O runner é {runner}')
    os.system("pause")

elif quantidade == 4:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)
    jogadores.append(player3)
    jogadores.append(player4)

    runner = random.choice(jogadores)
    runnerDouble = random.sample(jogadores, num_to_select)

    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runnerDouble}')
    os.system("pause")

elif quantidade == 5:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)
    jogadores.append(player3)
    jogadores.append(player4)
    jogadores.append(player5)

    runner = random.choice(jogadores)
    runnerDouble = random.sample(jogadores, num_to_select)

    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runnerDouble}')
    os.system("pause")

elif quantidade == 6:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')
    player6 = input('Insira o nome do sexto jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)
    jogadores.append(player3)
    jogadores.append(player4)
    jogadores.append(player5)
    jogadores.append(player6)

    runner = random.choice(jogadores)
    runnerDouble = random.sample(jogadores, num_to_select)
    runnerTriple = random.sample(jogadores, num_to_select3)

    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runnerDouble}')
    print(f'Caso tenha tres runners eles são: {runnerTriple}')
    os.system("pause")

elif quantidade == 7:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')
    player6 = input('Insira o nome do sexto jogador: ')
    player7 = input('Insira o nome do setimo jogador: ')

    jogadores.append(player1)
    jogadores.append(player2)
    jogadores.append(player3)
    jogadores.append(player4)
    jogadores.append(player5)
    jogadores.append(player6)
    jogadores.append(player7)

    runner = random.choice(jogadores)
    runnerDouble = random.sample(jogadores, num_to_select)
    runnerTriple = random.sample(jogadores, num_to_select3)

    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runnerDouble}')
    print(f'Caso tenha tres runners eles são: {runnerTriple}')
    os.system("pause")

else:
    print('O programa não chegou a tantas pessoas ainda: ')
    os.system("pause")
