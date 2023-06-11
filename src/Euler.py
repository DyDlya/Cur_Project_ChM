def get_data():
    print("|===========| Ввод данных |===========|")
    a, b = input("Введите границы интервала: ").split()
    h = float(input("Введите значение шага: "))
    y = float(input("Введите начальное значение функции: "))

    return float(a),float(b),h,y


def func(x, y):
    return (x**2) + (y**2)

def euler_method(f, h, y, a,b):
    x = a
    while x <= b:
        
        print(f"x = {x}, y = {round(y,4)}")

        y = y+ h * f(x,y)
        x = round(x+h, 4)

def main():
    a,b,h,y = get_data()
    print("\n|===========| Результаты вычислений |===========|")
    euler_method(func,h,y,a,b)


if __name__ == "__main__":
    main()
