import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row):
    result = []
    try:
        with open(dest, "r", encoding="utf-8") as f:
            lines = f.readlines()[int(num_row) - 1:int(num_row)]
        with open(source, "a", encoding="utf-8") as file:
            file.writelines(lines)
    except ValueError:
        try:
            with open(dest, "r", encoding="utf-8") as file_2:
                list_2 = file_2.readlines()
            result = [text for text in list_2 if num_row in text]
            if not result:
                print("По указанному значению совпадений не найдено")
            else:
                with open(dest, "r", encoding="utf-8") as file_1:
                    g = len(file_1.readline())
                    for i in range(g):
                        for j in range(len(file_1.readlines()[i - 1: i])):
                            if num_row == file_1.readlines()[i - 1: i][j - 1: j]:
                                result.append(file_1.readline()[i - 1: 1])
                with open(source, "a", encoding="utf-8") as file_3:
                    file_3.writelines(result)
        except ValueError:
            return


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
5 - завершение работы
"""

file = "Book.txt"
dest = "Add.txt"

if file not in os.listdir():
    print("указанное имя файла отсутствует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        num_row = input("Введите номер строки или имя из файла Add.txt для переноса в Book.txt: ")
        transfer_data(file, dest, num_row)
    elif mode == 5 or mode >=5:
        exit("Программа завершена")