numbers = [1234, 5678, 90]
file = open('file_with_list.txt', 'w')
print(numbers, end='', flush=True, file=file)
file.close()
