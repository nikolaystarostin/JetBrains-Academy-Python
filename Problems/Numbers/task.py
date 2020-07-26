# put your python code here
def multiply(a, b=1, *args):
    total = a * b
    for n in args:
        total *= n
    return total
