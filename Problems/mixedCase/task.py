words = (input() + ' ').split(' ', 1)
camel = words[0] + words[1].title().replace(' ', '')
print(camel)
