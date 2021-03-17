import os
import shutil

task = input("Какую операцию вы хотите выполнить?\n"
             "1. Создание папки (с указанием имени);\n"
             "2. Удаление папки по имени;\n"
             "3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;"
             "\n"
             "4. Создание пустых файлов с указанием имени;\n"
             "5. Запись текста в файл;\n"
             "6. Просмотр содержимого текстового файла;\n"
             "7. Удаление файлов по имени;\n"
             "8. Копирование файлов из одной папки в другую;\n"
             "9. Перемещение файлов;\n"
             "10. Переименование файлов;\n"
             "11. Вывести текущую директорию;\n"
             "12. Вывести все список всех файлов и папок;\n"
             "13. Создание вложенных папок.\n"
             "Выберите номер операции: ")


# Создание папки (с указанием имени)
def task1(name_mkdir):
    os.mkdir(name_mkdir)


# Удаление папки по имени
def task2(del_name_mkdir):
    os.rmdir(del_name_mkdir)


# Перемещение между папками
def task3(ch_dir_name):
    os.chdir(ch_dir_name)
    print("Текущая директория изменилась на: ", os.getcwd())


# Создание пустых файлов с указанием имени
def task4(name_file):
    open(str(name_file) + ".txt", "w")


# Запись текста в файл
def task5(text_name_file, text):
    text_name_file = open(text_name_file, "w")
    text_name_file.write(text)


# Просмотр содержимого текстового файла
def task6(name_file):
    name_file = open(name_file, "r")
    print(name_file.read())


# Удаление файлов по имени
def task7(name_file):
    os.remove(name_file)


# Копирование файлов из одной папки в другую
def task8(name_file, name_dir):
    shutil.copy(name_file, name_dir)


# Перемещение файлов
def task9(name_file, name_dir):
    os.replace(name_file, name_dir + "/" + name_file)


# Переименование файлов
def task10(name_file, new_name):
    os.rename(name_file, new_name + ".txt")


while True:
    if 1 <= int(task) <= 10:
        if int(task) == 1:
            name_mkdir = input("Введите название папки, которую хотите создать: ")
            task1(name_mkdir)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 2:
            del_name_mkdir = input("Введите название папки, которую хотите удалить: ")
            task2(del_name_mkdir)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 3:
            print("Текущая директория: ", os.getcwd())
            ch_dir_name = input("Введите название папки, в которую хотите перейти:\n"
                                "Примечание: если вы хотите вернуться на одну папку назада просто введите ..\n"
                                "")
            task3(ch_dir_name)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 4:
            name_file = input("Введите название файла: ")
            task4(name_file)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 5:
            text_name_file = input("Введите название файла, куда хотите записать текст: ")
            text = input("Введите текст, который хотите записать в файле: ")
            task5(text_name_file, text)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 6:
            name_file = input("Введите название файла, у которого хотите просмотреть содержимое: ")
            task6(name_file)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 7:
            name_file = input("Введите название файла, который хотите удалить: ")
            task7(name_file)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 8:
            name_file = input("Введите название файла, который хотите скопировать: ")
            name_dir = input("Введите название каталога, в которого хотите скопировать файл: ")
            task8(name_file, name_dir)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 9:
            name_file = input("Введите название файла, который хотите переместить: ")
            name_dir = input("Введите название каталога, в которого хотите переместить файл: ")
            task9(name_file, name_dir)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")

        if int(task) == 10:
            name_file = input("Введите название файла, который хотите переименовать: ")
            new_name = input("Введите новое название файла: ")
            task10(name_file, name_dir)
            operation = input("Если вы хотите продолжить, то введите номер операции, который хотите выполнить;\n"
                              "Если хотите завершить, то введите слово exit: ")
            if operation.isdigit():
                task = operation
            elif operation == "exit":
                break
            else:
                print("Введено в некорректном формате!")