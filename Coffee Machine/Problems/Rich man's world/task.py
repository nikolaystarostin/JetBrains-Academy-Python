x = int(input())
years = 0
while x <= 700000:
    x *= 1.071
    years += 1
print(years)
