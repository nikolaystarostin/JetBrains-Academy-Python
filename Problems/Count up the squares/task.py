sum_sq = 0
sum_n = 0
i = 0
while sum_n != 0 or i == 0:
    n = int(input())
    sum_sq += n ** 2
    sum_n += n
    i += 1
print(sum_sq)
