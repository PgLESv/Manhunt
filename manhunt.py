import random
import os

print('ALEATORIZADOR DE TIMES DO MANHUNT')

quantidade = int(input('Insira quantos jogadores irão jogar: '))

if quantidade <= 1:
    print ('Não tem como jogar com uma pessoa!')
    os.system("pause")

elif quantidade == 2:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')

    runner = random.choice([player1, player2])
    print(f'O runner é {runner}')
    os.system("pause")

elif quantidade == 3:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')

    runner = random.choice([player1, player2, player3])
    print(f'O runner é {runner}')
    os.system("pause")

elif quantidade == 4:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')

    runner = random.choice([player1, player2, player3, player4])
    runnerDouble = random.choice([player1, player2, player3, player4])
    while runnerDouble == runner:
        runnerDouble = random.choice([player1, player2, player3, player4])
    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runner, runnerDouble}')
    os.system("pause")

elif quantidade == 5:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')

    runner = random.choice([player1, player2, player3, player4, player5])
    runnerDouble = random.choice([player1, player2, player3, player4, player5])
    while runnerDouble == runner:
        runnerDouble = random.choice([player1, player2, player3, player4, player5])
    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runner, runnerDouble}')
    os.system("pause")

elif quantidade == 6:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')
    player6 = input('Insira o nome do sexto jogador: ')

    runner = random.choice([player1, player2, player3, player4, player5, player6])
    runnerDouble = random.choice([player1, player2, player3, player4, player5, player6])
    runnerTriple = random.choice([player1, player2, player3, player4, player5, player6])
    while runnerDouble == runner:
        runnerDouble = random.choice([player1, player2, player3, player4, player5, player6])
    while runnerTriple == runner and runnerDouble:
        runnerTriple = random.choice([player1, player2, player3, player4, player5, player6])
    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runner, runnerDouble}')
    print(f'Caso tenha tres runners eles são: {runner, runnerDouble, runnerTriple}')
    os.system("pause")

elif quantidade == 7:
    player1 = input('Insira o nome do primeiro jogador: ')
    player2 = input('Insira o nome do segundo jogador: ')
    player3 = input('Insira o nome do terceiro jogador: ')
    player4 = input('Insira o nome do quarto jogador: ')
    player5 = input('Insira o nome do quinto jogador: ')
    player6 = input('Insira o nome do sexto jogador: ')
    player7 = input('Insira o nome do setimo jogador: ')

    runner = random.choice([player1, player2, player3, player4, player5, player6, player7])
    runnerDouble = random.choice([player1, player2, player3, player4, player5, player6, player7])
    runnerTriple = random.choice([player1, player2, player3, player4, player5, player6, player7])
    while runnerDouble == runner:
        runnerDouble = random.choice([player1, player2, player3, player4, player5, player6, player7])
    while runnerTriple == runner and runnerDouble:
        runnerTriple = random.choice([player1, player2, player3, player4, player5, player6, player7])
    print(f'O runner é {runner}')
    print(f'Caso tenha dois runners eles são: {runner, runnerDouble}')
    print(f'Caso tenha tres runners eles são: {runner, runnerDouble, runnerTriple}')
    os.system("pause")

else:
    print('O programa não chegou a tantas pessoas ainda: ')
    os.system("pause")