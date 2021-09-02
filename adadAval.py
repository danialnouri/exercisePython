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
print(adadaval(n))
