from scipy.optimize import root
from numpy import log

def exit():
    input("\nНажмите любую кнопку для выхода.")

# Уравнение
def func(x):
    return (log(x)*log(x)-(1/x))
    
# Производная уравнения
def derivFunc(x):
    return ((2*x*log(x)+1)/(x*x))
    
# Метод дихотомии (половинного деления)
def bisec_method(a, b, epsilon):
    a0 = a
    b0 = b
    if (func(a) * func(b) >= 0):
        print("Неправильно определены a и b\n")
        return

    c = a
    while ((b - a) >= epsilon):
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
    print("Корень: ", c)
    with open("result.txt", "w") as f:
        f.writelines(["Метод дихотомии (половинного деления) (a = {}, b = {}, epsilon = {}): \n".format(a0, b0, epsilon), "Корень: {}".format(c)])
    
# Метод Ньютона
def newton_method(x, epsilon):
    x0 = x
    h = func(x) / derivFunc(x)
    while abs(h) >= epsilon:
        h = func(x) / derivFunc(x)
        # Формула Ньютона:
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        
        if x <= 0:
            print("Значение вышло за ОДЗ функции при итерации.")
            x = "не найден"
            break
     
    print("Корень: ", x)
    with open("result.txt", "w") as f:
        f.writelines(["Метод Ньютона (x0 = {}, epsilon = {}): \n".format(x0, epsilon), "Корень: {}\n".format(x)])

# Метод простых итераций
def simple_iter_method(x0):
    res = root(lambda x: func(x), x0=x0)
    if (res.success == True):
        print("Корень: ", res.x[0])
        with open("result.txt", "w") as f:
            f.writelines(["Метод простых итераций (x0 = {}): \n".format(x0), "Корень: {}\n".format(res.x[0])])
    else:
        print("Корень: не найден.")
        with open("result.txt", "w") as f:
            f.writelines(["Метод простых итераций (x0 = {}): \n".format(x0), "Корень: не найден"])

def main():
   try:
    print("Задача №1\nУравнение: ln(x)^2-(1/x)\n\nВыберите метод:\n1) Метод дихотомии (половинного деления)\n2) Метод простых итераций\n3) Метод Ньютона")
    choose = input("(1, 2, 3): ")

    # Метод дихотомии (половинного деления)
    if (choose == "1"):
        a = input("Введите значение границы a: ")
        b = input("Введите значение границы b: ")
        epsilon = input("Введите значение абсолютной погрешности (например, 0.01): ")
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
        epsilon = input("Введите значение абсолютной погрешности (например, 0.01): ")
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