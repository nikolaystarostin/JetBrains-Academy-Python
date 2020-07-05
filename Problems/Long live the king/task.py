x = int(input())
y = int(input())

if 2 <= x <= 7:
    if 2 <= y <= 7:
        print(8)
    else:
        print(5)
else:
    if 2 <= y <= 7:
        print(5)
    else:
        print(3)
