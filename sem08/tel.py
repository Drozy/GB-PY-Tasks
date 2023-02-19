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
        data = file.readlines()
    return data


def write_data(data):
    with open('sem08/handbook.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


def add_entry(data):
    data.append('\n' + input('Введите новую запись: '))


def screen(data):
    for elem in data:
        print(elem.strip())


def find_entry(data):
    pass


def menu():
    pass


def main():
    data = read_data()
    screen(data)
    # menu()
    add_entry(data)
    # screen(data)
    write_data(data)


if __name__ == '__main__':
    main()
