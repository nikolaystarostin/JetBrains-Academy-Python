# put your python code here
a = int(input())
b = int(input())

sum_ = 0
n = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sum_ += i
        n += 1

print(sum_ / n)
