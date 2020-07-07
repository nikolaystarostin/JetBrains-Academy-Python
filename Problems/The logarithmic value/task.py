import math

a = float(input())
b = float(input())

if b <= 0 or b == 1.0:
    print(round(math.log(a), 2))
else:
    print(round(math.log(a, b), 2))
