number = [int(x) for x in input()]
ma = [(number[x] + number[x + 1]) / 2 for x in range(len(number) - 1)]
print(ma)
