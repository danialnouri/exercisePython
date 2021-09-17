def adadaval(n):
    k = 1
    count = 0
    while k <= n:
        if n % k == 0:
            count += 1
        k += 1
    if count == 2:
        return True
    else:
        return False


n = int(input('enter a number:'))
k = 1

while k <= n:
    if adadaval(k):
        print(k)
    k += 2
