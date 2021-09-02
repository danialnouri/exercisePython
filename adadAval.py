n = int(input('enter the range:'))
k = 1
count = 0
while k <= n:
    if n % k == 0:
        count += 1
    k += 1
if count == 2:
    print("yes")
else:
    print("no")
