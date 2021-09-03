def adadavalyab(n):
    k=1
    tedad=0
    while k<=n:
        if n%k==0:
            tedad+=1
        k += 1
    if tedad == 2:
       return True
    else:
       return False


n=int (input("yek adad vared knid:"))
print(adadavalyab(n))
