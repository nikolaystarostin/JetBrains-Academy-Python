# the list "walks" is already defined
distance = 0
for day in walks:
    distance += day['distance']
print(round(distance / len(walks)))
