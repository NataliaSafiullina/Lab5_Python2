import pymysql
import cryptography


def update_dict(dic, word):
    # если такой ключ есть в словаре прибавим количество
    # если нет - добавим ключ и значение
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1


def connect_mysql():
    connect = pymysql.connect(host="127.0.0.1",
                              user="root",
                              password="pass",
                              db="balance")
    print("MySQL's connected", end='\n\n')
    return connect


if __name__ == '__main__':

    while True:
        option = int(input('Опции: \n'
                           '1 - Палиндром \n'
                           '2 - Минимумы \n'
                           '3 - Персонажи \n'
                           '4 - MySQL \n'
                           'Введите номер опции: '))

        match option:
            case 1:

                # Задача 1 - Палиндром

                # пользователь вводит строку
                a = input('Задача1. Введите строку: ')

                print('Вариант 1')

                # сохраним перевернутую строку
                b = a[::-1]
                # сравниваем строки заменив пробелы переведя в нижний регистр
                if a.replace(' ', '').lower() == b.replace(' ', '').lower():
                    print('Да')
                else:
                    print('Нет')

                print('Вариант 2')

                a = a.replace(' ', '').lower()
                i, j = 0, len(a) - 1
                while i < j:
                    if a[i] != a[j]:
                        print('Нет')
                        break
                    i += 1
                    j -= 1
                else:
                    print('Да')

                print('Вариант 3')

                print('Да' * (a.replace(' ', '').lower() == a[::-1].replace(' ', '').lower()),
                      'Нет' * (a.replace(' ', '').lower() != a[::-1].replace(' ', '').lower()))
            case 2:

                # Задача 2 - Минимумы
                print('Задача2. Вводите прямоугольную матрицу через пробел (end - чтобы закончить ввод):')
                a = []
                while 1:
                    x = [c for c in input().split()]
                    if x[0] == 'end':
                        break
                    a.append([int(j) for j in x])

                minimums = 0
                for i in a:
                    minimums = i[0]
                    for j in i:
                        if j < minimums:
                            minimums = j
                    print(minimums)

                minimums = 0
                for i in a:
                    minimums = min(i)
                    print(minimums)

            case 3:

                # Задача 3 - Подсчёт персонажей
                # пустой словарь
                d = {}
                # ввод строки с клавиатуры слова разделены пробелами
                # обновременная запись в словарь
                print('Задача3. Вводим имена через пробел.')
                str = {update_dict(d, word) for word in input().lower().split()}
                i = 0
                for key, value in d.items():
                    i += 1
                    print(i, ') ', key, ': ', value)

            case 4:

                print('Задача4. MySQL')
                con = connect_mysql()
                sql = "select employee_name, employee_position from employees where employee_id > %s"
                i = input('Введите ID: ')
                cur = con.cursor()
                cur.execute(sql, i)
                for r in cur:
                    print(r[0], '\t', r[1])

            case _:
                break
