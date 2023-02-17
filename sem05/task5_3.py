# Создайте программу для игры в "Крестики-нолики".

# Победные линии (индексы полей)
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]

# Инициализация доски
deck = [str(i + 1) for i in range(9)]

# Вывод доски
def printDeck():
    print()
    for i in range(9):
        print(deck[i], end='  ')
        if (i + 1) % 3 == 0:
            print()
    print()

# Ход игрока
def playerTurn(who_turns):
    if not who_turns:
        symbol = 'X'
    else:
        symbol = 'O'
    print(f'Ходит {symbol}.')
    while True:
        move = int(input('Введите номер поля: '))
        if 0 < move < 10 and deck[move - 1].isdigit():
            break
        else:
            print('Неверный ввод! Попробуйте ещё раз.')
    deck[move - 1] = symbol

# Ход бота
def BotTurn():
    move = checkLines(2, 0)        # проверка линий на наличие двух О, чтобы сделать ход и выиграть
    if not move:
        move = checkLines(0, 2)    # проверка линий на наличие двух Х, чтобы не дать выиграть игроку
    if not move:
        move = checkLines(1, 0)    # поиск линии с одним О, без Х
    if not move:                   # если предыдущие проверки провалились, можно попробовать занять центр
        if deck[4].isdigit():
            move = 5
    if not move:                   # когда умных вариантов не осталось, ход в свободное поле
        for i in range(9):
            if deck[i].isdigit():
                move = i + 1
    print(f'Ходит O.\nБот выбирает поле {move}')
    deck[move - 1] = 'O'

# Проверка линий на количество О и Х для умных ходов
def checkLines(sum_o, sum_x):
    move = 0
    for line in win_lines:
        o = 0
        x = 0
        for j in range(3):
            if deck[line[j]] == 'O':
                o += 1
            if deck[line[j]] == 'X':
                x += 1
        if o == sum_o and x == sum_x:
            for j in range(3):
                if deck[line[j]].isdigit():
                    move = int(deck[line[j]])
    return move

# Проверка результата игры
def whoWins():
    winner = ''
    for line in win_lines:
        if deck[line[0]] == 'X' and deck[line[1]] == 'X' and deck[line[2]] == 'X':
            winner = 'X'
        if deck[line[0]] == 'O' and deck[line[1]] == 'O' and deck[line[2]] == 'O':
            winner = 'O'
    return winner


def main():
    print('----- КРЕСТИКИ - НОЛИКИ -----')
    mode = int(input('Выберите режим игры: \n Игрок против игрока (0) \n Игрок против бота (1)\n'))
    printDeck()
    winner = ''
    count = 0
    who_turns = 0
    while winner == '' and count < 9:
        if not who_turns:
            playerTurn(who_turns)
        elif mode:
            BotTurn()
        else:
            playerTurn(who_turns)
        printDeck()
        winner = whoWins()
        count += 1
        who_turns = count % 2
    if count == 9 and winner == '':
        print('Ничья!')
    else:
        print('Победа за', winner)


if __name__ == "__main__":
    main()
