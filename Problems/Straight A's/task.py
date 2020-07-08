grades = input().split()
grades_a = [1 for x in range(len(grades)) if grades[x] == 'A']
print(round(len(grades_a) / len(grades), 2))
