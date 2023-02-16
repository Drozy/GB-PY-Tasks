# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint


def playerTurn(player):
    turn = 0
    print(f'Игрок {player}, твой ход.')
    while not 0 < turn < turn_limit+1:
        turn = int(input(f'Возьми от 1 до {turn_limit} конфет: '))
    return turn


def botTurn(amt, ai):
    if ai:
        d = amt % (turn_limit + 1)  # стратегия победы
        if d == 0:
            turn = randint(1, turn_limit)
        else:
            turn = d
    else:
        turn = randint(1, turn_limit)
    print(f'Бот взял {turn} конфет.')
    return turn


def game(amt, mode, diff):
    print('Определяю, за кем первый ход... (Нажмите "Enter")')
    input()
    who_turns = randint(0, 1)   # 1 - ходит 1 игрок, 0 - ходит 2 игрок(бот)
    while amt > turn_limit:
        print(f'---------------------------------\nНа столе лежат {amt} конфет.')
        if who_turns:
            amt -= playerTurn(pl1)
            who_turns = 0
        else:
            if mode:
                amt -= botTurn(amt, diff)
            else:
                amt -= playerTurn(pl2)
            who_turns = 1
    return who_turns


amount = 2021
turn_limit = 28

mode = int(input('Выберите режим игры: \n Игрок против игрока (0) \n Игрок против бота (1)\n'))
pl1 = input('Игрок 1, назовись: ')
if mode:
    diff = int(input('Выберите сложность: \n (0) - Обычная \n (1) - Невозможная\n'))
    pl2 = 'Бот'
else:
    diff = 0
    pl2 = input('Игрок 2, назовись: ')

who_win = game(amount, mode, diff)

if who_win:
    print(f'{pl1} забирает все!')
else:
    print(f'{pl2} забирает все!')
