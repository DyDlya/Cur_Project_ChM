def func(x, y):
    return (x**2) + (y**2)

def euler_method(f, h, y, a,b):
    x = a
    while x <= b:
        
        print(f"x = {x}, y = {y}")

        y = y+ h * f(x,y)
        x = round(x+h, 4)

euler_method(func, 0.1, 1, 0, 5) 

    