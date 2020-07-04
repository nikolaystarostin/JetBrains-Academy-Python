scores = input().split()
# put your python code here
lives = 0
score = 0

for i in scores:
    if i == 'I':
        lives += 1
    if lives >= 3:
        print('Game over')
        print(score)
        break
    if i == 'C':
        score += 1
else:
    print('You won')
    print(score)
