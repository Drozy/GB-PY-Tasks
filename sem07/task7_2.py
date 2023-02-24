# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)

# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[operation(i + 1, j + 1) for j in range(num_columns)]
             for i in range(num_rows)]
    # расчёт максимальной длины колонок
    max_columns = []
    for col in zip(*table):
        len_el = []
        [len_el.append(len(str(el))) for el in col]
        max_columns.append(max(len_el))
    # печать таблицы
    for row in table:
        for col in row:
            print(f'{col:{max(max_columns)+1}}', end=' ')
        print()
    print()


def main():
    print_operation_table(lambda x, y: x * y)
    print_operation_table(lambda x, y: 7 * (x - 1) + y, 5, 7)


if __name__ == '__main__':
    main()
