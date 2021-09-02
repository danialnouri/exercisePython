n = int(input("enter a number:"))
while n != 0:
    r = n % 10
    print(r, end='')
    n = int(n / 10)
