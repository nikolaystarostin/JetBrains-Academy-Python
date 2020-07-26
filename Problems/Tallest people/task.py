def tallest_people(**kwargs):
    for key in sorted([x for x in kwargs.keys() if kwargs[x] == max(kwargs.values())]):
        print(f'{key} : {kwargs[key]}')
