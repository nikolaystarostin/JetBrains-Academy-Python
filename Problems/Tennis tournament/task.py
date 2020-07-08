n = int(input())
result = []
for i in range(n):
    line = input().split()
    result.append(line)
wins = [result[x][0] for x in range(len(result)) if result[x][1] == 'win']
print(wins)
print(len(wins))
