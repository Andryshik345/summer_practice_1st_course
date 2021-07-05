from scipy.optimize import linearmixing
from numpy import log

def exit():
    input("\nНажмите любую кнопку для выхода.")

# Уравнение
def func(x):
    return (log(x)*log(x)-(1/x))
    
# Производная уравнения
def derivFunc(x):
    return ((2*x*log(x)+1)/(x*x))
    
# Очень глупая ф-ция для проверки округления
def check_round(n):
    if ('.' in str(n)):
        return len(str(n)) - 2
    elif ('e' in str(n)):
        return int(str(n).split('-')[1])
    
# Метод дихотомии (половинного деления)
def bisec_method(a, b, epsilon):
    a0 = a
    b0 = b
    if (func(a) * func(b) >= 0):
        print("Неправильно определены a и b\n")
        return

    c = a
    i = 0
    while ((b - a) >= epsilon):
        # Тикаем счетчик
        i += 1
        # Находим среднюю точку
        c = (a + b) / 2
        # Проверяем, если средняя точка - корень
        if (func(c) == 0.0):
            break
        # Определяем путь повторения шагов
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c
    # Округляем корень до разрядов из epsilon
    res = round(c, check_round(epsilon))
    print("Корень: ", res)
    print("Итераций: ", i)
    print("Значение функции: ", func(c))
    # Запись в файл
    with open("result.txt", "w") as f:
        f.writelines(["Метод дихотомии (половинного деления) (a = {}, b = {}, epsilon = {}): \n".format(a0, b0, epsilon),
                    "Корень: {}\n".format(res),
                    "Итераций: {}\n".format(i),
                    "Значение функции: {}".format(func(c))])
    
# Метод Ньютона
def newton_method(x, epsilon):
    x0 = x
    i = 0
    flag = True
    h = func(x) / derivFunc(x)
    while abs(h) >= epsilon:
        # Тикаем счетчик
        i += 1
        h = func(x) / derivFunc(x)
        # Формула Ньютона:
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        
        if x <= 0:
            print("Значение вышло за ОДЗ функции при итерации.")
            x = "не найден"
            flag = False
            # Запись в файл
            with open("result.txt", "w") as f:
                f.writelines(["Метод Ньютона (x0 = {}, epsilon = {}): \n".format(x0, epsilon),
                    "Корень: не найден (значение вышло за ОДЗ функции при итерации.)\n",
                    "Итераций: {}\n".format(i),
                    "Значение функции: нет"])
            break

    if (flag == True):
        res = round(x, check_round(epsilon))
        print("Корень: ", res)
        print("Итераций: ", i)
        print("Значение функции: ", func(x))
        # Запись в файл
        with open("result.txt", "w") as f:
            f.writelines(["Метод Ньютона (x0 = {}, epsilon = {}): \n".format(x0, epsilon),
                        "Корень: {}\n".format(res),
                        "Итераций: {}\n".format(i),
                        "Значение функции: {}".format(func(x))])

# Метод простых итераций
def simple_iter_method(x0):
   try:
    res = linearmixing(lambda x: func(x), xin=x0, maxiter=500)
   except Exception:
    print("\nКорень: не найден (отсутствие сходимости).")
    # Запись в файл
    with open("result.txt", "w") as f:
        f.writelines(["Метод простых итераций (x0 = {}): \n".format(x0),
                    "Корень: не найден (отсутствие сходимости).",
                    "Итераций: нет",
                    "Значение функции: нет"])
   else:
    print("\nКорень: ", res.x[0])
    # Запись в файл
    with open("result.txt", "w") as f:
        f.writelines(["Метод простых итераций (x0 = {}): \n".format(x0),
                    "Корень: {}".format(res.x[0]),
                    "Итераций: {}".format(res.nit),
                    "Значение функции: {}".format(func(res.x[0]))])

def main():
   try:
    print("Задача №1\nУравнение: ln(x)^2-(1/x)\n\nВыберите метод:\n1) Метод дихотомии (половинного деления)\n2) Метод простых итераций\n3) Метод Ньютона")
    choose = input("(1, 2, 3): ")

    # Метод дихотомии (половинного деления)
    if (choose == "1"):
        a = input("Введите значение границы a: ")
        b = input("Введите значение границы b: ")
        epsilon = input("Введите значение абсолютной погрешности (например, 0.01 либо 1e-12): ")
        if (a > "0" and b > "0"):
            bisec_method(int(a), int(b), float(epsilon))
        else:
            print("В данном случае интервал не может быть меньше или равным нулю (логарифм принимает только положительные знач-я).")

    # Метод простых итераций
    elif (choose == "2"):
        x0 = input("Введите значение x0 (начального приближения): ")
        if (x0 > "0"):
            simple_iter_method(float(x0))
        else:
            print("Значение x0 не может быть меньше или равным нулю (логарифм принимает только положительные знач-я).")

    # Метод Ньютона
    elif (choose == "3"):
        x0 = input("Введите значение x0 (начального приближения): ")
        epsilon = input("Введите значение абсолютной погрешности (например, 0.01 либо 2e-12): ")
        if (epsilon == "0"):
            print("В данном случае значение абсолютной погрешности не может быть равно нулю.")
            exit()
        if (x0 > "0"):
            newton_method(int(x0), float(epsilon))
        else:
            print("Значение x0 не может быть меньше или равным нулю (логарифм принимает только положительные знач-я).")

    else:
        print("Неверный выбор либо пустой ввод.")

    exit()
   except Exception as ex:
    print("Произошла ошибка (возможно неверный или пустой ввод): ", ex)

if __name__ == "__main__":
    main()