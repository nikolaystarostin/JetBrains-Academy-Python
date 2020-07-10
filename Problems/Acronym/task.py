file = open('test.txt')
lines = file.readlines()
rows = len(lines)
for i in range(rows):
    print(lines[i][0])
file.close()
