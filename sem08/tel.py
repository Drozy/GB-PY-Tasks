# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.


def read_data():
    with open('sem08/handbook.txt', 'r', encoding='utf-8') as file:
        rawdata = file.readlines()
        data = [i.strip().split(';') for i in rawdata]
    return data


def write_data(data):
    text = ''
    for row in data:
        text += ';'.join(row) + '\n'
    with open('sem08/handbook.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def add_entry(data):
    data.append(input('Введите новую запись в формате "Фамилия Имя Отчество Телефон":\n').split())


def print_dir(data):
    max_columns = []
    for col in zip(*data):
        len_el = []
        [len_el.append(len(el)) for el in col]
        max_columns.append(max(len_el))
    print()    
    for row in data:
        for n, col in enumerate(row):
            print(f'{col:{max_columns[n]+1}}', end='  ')
        print()
    print()


def find_entry(data):
    sign = input('Кого вы хотите найти?\n')
    flag = 1
    for row in data:
        if sign in row:
            print(' '.join(row))
            flag = 0
    if flag:
        print('Такой записи нет в справочнике.')


# Удаляет первую запись, содержащую введенное значение
def del_entry(data):
    sign = input('Кого вы хотите удалить из справочника?\n')
    flag = 1
    for i in range(len(data)):
        if sign in data[i]:
            print(' '.join(data[i]))
            del data[i]
            print(f'Запись, содержащая "{sign}" удалена.')
            flag = 0
            break
    if flag:
        print('Такой записи нет в справочнике.')


def edit_entry(data):
    sign = input('Чью запись вы хотите отредактировать?\n')
    flag = 1
    num = -1
    for i in range(len(data)):
        if sign in data[i]:
            print(' '.join(data[i]))
            num = i
            flag = 0
            break
    if flag:
        print('Такой записи нет в справочнике.')
    if num >= 0:
        data[num] = input('Введите новые данные в формате "Фамилия Имя Отчество Телефон":\n').split()


def menu():
    actions = {
            1: print_dir,
            2: add_entry,
            3: find_entry,
            4: edit_entry,
            5: del_entry,
            0: 'exit'
    }
    while True:
        try:
            choice = int(input('\nВыберите действие:\n' +
            '(1) - Вывести справочник\n' +
            '(2) - Добавить новую запись\n' +
            '(3) - Найти человека в справочнике\n' +
            '(4) - Изменить запись\n' +
            '(5) - Удалить запись\n' +
            '(0) - Выход\n'))
            if -1 < choice < 6:
                break
            else:
                print('Неверный ввод, попробуйте ещё раз.\n')
        except Exception:
            print('Неверный ввод, попробуйте ещё раз.\n')
    print()
    return actions.get(choice)


def doAction(action, data = None):
    if action == 'exit':
        write_data(data)
        exit()
    else:
        action(data)


def main():
    data = read_data()
    while True:
        doAction(menu(), data)


if __name__ == '__main__':
    main()
