import math


def area(r):
    return math.pi * r ** 2


def environment(r):
    return 2 * math.pi * r


r = int(input("megdar shoae dayere ra vared knid:"))
print("masahat:",  area(r))
print("mohit:", environment(r))
