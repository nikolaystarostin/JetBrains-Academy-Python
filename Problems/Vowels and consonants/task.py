word = input()

vowel = 'aeiou'

for i in word:
    if not i.isalpha():
        break
    elif i in vowel:
        print('vowel')
    else:
        print('consonant')
