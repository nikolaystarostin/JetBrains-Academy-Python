cafe = input().split()
best = cafe
while cafe[0] != 'MEOW':
    cafe = input().split()
    if cafe[0] != 'MEOW':
        if int(cafe[1]) > int(best[1]):
            best = cafe
print(best[0])
