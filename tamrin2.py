def area(x, y):
    return x * y


def enviroment(x, y):
    return 2 * (x + y)


x = int(input('enter height:'))
y = int(input('enter width:'))
print(area(x, y))
print(enviroment(x, y))
