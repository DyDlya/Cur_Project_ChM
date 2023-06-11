def get_data():
    print("|===========| Ввод данных |===========|")
    a, b = input("Введите границы интервала: ").split()
    h = float(input("Введите значение шага: "))
    y = float(input("Введите начальное значение функции: "))

    return float(a),float(b),h,y

def f(x, y): 
 # Это функция, которую нужно решить 
 # Вам нужно определить эту функцию перед использованием метода Рунге-Кутта 
 # Пример: return x2 + y2 
        return x**2 + y**2

def runge_method(x0, y0, h, xn): 
     
 
    i= x0 + round(h,2) 
    while i <= xn: 
        k0 = f(i, y0)*h 
        k1 = f(i + h / 2, y0 +  k0 / 2) *h
        k2 = f(i + h / 2, y0 + k1 / 2)  *h
        k3 = f(i + h , y0 + k2 ) *h
        y = y0 + 1/6 * h * (k0 + 2*k1 + 2*k2 + k3) 
        print(f"при x={round(i,2)}, y={round(y,4)}") 
        y0 = y0 + h * f(i, y0) 
        i+= round(h, 2) 
 
 
def main():
    a,b,h,y = get_data()
    print("\n|===========| Результаты вычислений |===========|")
    runge_method(a,y,h,b)


if __name__ == "__main__":
    main()