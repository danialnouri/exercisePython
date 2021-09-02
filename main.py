n = int(input('enter the range:'))
k = 1
sum_magsum = 0
while k < n:
    if n % k == 0:
        sum_magsum += k
    k += 1
if sum_magsum == n:
    print('its perfect number')
else:
    print('its not perfect number')
