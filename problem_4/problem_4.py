def exit():
    input("\nНажмите любую кнопку для выхода.")

# Функция для складывания элементов в несколько строк
def transfer_array_str(n):
    a = ""
    for line in n:
        a += line + "\n"
    return a

# Функция для чтения строк из файла и удаления '\n' символов
def read_file():
    text = ""
    with open("source.txt", "r") as f:
        text = f.readlines()
    # Парсим элементы и убираем '\n'
    for i in range(len(text)):
        edit_text = text[i].replace("\n", "")
        text[i] = edit_text
    return text

# Метод "Поиск и замена строк из набора" (найти - заменить на)
def search_string(needed, change):
    text = read_file()
    orig_text = "\nИсходный текст: \n" + transfer_array_str(text)
    print(orig_text)
    # В цикле парсим все элементы массива и меняем найденные подстроки на заменяемые
    for i in range(len(text)):
        edit = text[i].replace(needed, change)
        text[i] = edit
    print("\nИзмененный текст: \n" + transfer_array_str(text))
    # Запись в файл на диск
    with open("result.txt", "w") as f:
        f.writelines(['Метод "Поиск и замена строк из набора"\n', "\nНайти: {}\nЗаменить на: {}\n".format(needed, change),
                    orig_text,
                    "\nИзмененный текст: \n{}".format(transfer_array_str(text))])

# Метод "Нахождение частоты повторения строки"
def count_lines(needed):
    text = read_file()
    c = 0
    # В цикле парсим все элементы массива и подсчитываем кол-во повторений идентичных строк
    for i in range(len(text)):
        if needed == text[i]:
            c += 1
    print("\nИсходный текст: \n" + transfer_array_str(text))
    print("Количество повторений строки: " + str(c))
    # Запись в файл на диск
    with open("result.txt", "w") as f:
        f.writelines(['Метод "Нахождение частоты повторения строки"\n', "\nНайти: {}\n".format(needed),
                    "\nИсходный текст: \n" + transfer_array_str(text),
                    "\nКоличество повторений строки: " + str(c)])

# Метод "Вставка заданной строки после найденной"
def paste_str(needed):
    text = read_file()
    mask = []
    # В цикле парсим все элементы массива, находим индекс введенной строки, потом "склеиваем" первую половину массива, нужную строку и вторую половину массива.
    for i in range(len(text)):
        if needed == text[i]:
            mask += (text[:i])
            mask.append(needed)
            mask += (text[i:])
            # Т.к. добавляем сразу после первой же найденной строки, то нужно досрочно завершать цикл
            break
    print("\nИсходный текст: \n" + transfer_array_str(text))
    print("\nИзмененный текст: \n" + transfer_array_str(mask))
    # Запись в файл на диск
    with open("result.txt", "w") as f:
        f.writelines(['Метод "Вставка заданной строки после найденной"\n', "\nНайти: {}\n".format(needed),
                    "\nИсходный текст: \n" + transfer_array_str(text),
                    "\nИзмененный текст: \n" + transfer_array_str(mask)])

def main():
   try:
    # Проверяем, если исходный файл с текстом существует
    try:
        text = transfer_array_str(read_file())
    except:
        print("Файл source.txt не существует.")
        return
    print("Задача №4\nИсходный текст:\n{}\nВыберите метод:\n1) Поиск и замена строк из набора\n2) Нахождение частоты повторения строки\n3) Вставка заданной строки после найденной\n".format(text))
    choose = int(input("(1, 2, 3): "))
    
    # Метод "Поиск и замена строк из набора"
    if (choose == 1):
        needed = input("Найти: ")
        change = input("Заменить на: ")
        if (needed and change):
            search_string(needed, change)
        else:
            print("Пустой ввод.")

    # Метод "Нахождение частоты повторения строки"
    elif (choose == 2):
        needed = input("Найти: ")
        if (needed):
            count_lines(needed)
        else:
            print("Пустой ввод.")

    # Метод "Вставка заданной строки после найденной"
    elif (choose == 3):
        needed = input("Найти: ")
        if (needed):
            paste_str(needed)
        else:
            print("Пустой ввод.")

    else:
        print("Неверный выбор либо пустой ввод.")
        
    exit()
   except Exception as ex:
    print("Произошла ошибка (возможно неверный или пустой ввод): ", ex)
    
if __name__ == "__main__":
    main()