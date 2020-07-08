prime_numbers = []
for i in range(2, 1001):
    remainders = [i % x for x in range(2, i)]
    if all(remainders):
        prime_numbers.append(i)
