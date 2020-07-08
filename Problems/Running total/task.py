number = input()
number_list = [int(x) for x in number]
sum_list = [sum(number_list[0:x]) for x in range(0, len(number_list) + 1)]
sum_list.pop(0)
print(sum_list)
