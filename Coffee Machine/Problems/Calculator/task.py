a = float(input())
b = float(input())
op = input()


if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("Division by 0!")
elif op == 'mod':
    if b != 0:
        print(a % b)
    else:
        print("Division by 0!")
elif op == 'pow':
    print(a ** b)
elif op == 'div':
    if b != 0:
        print(a // b)
    else:
        print("Division by 0!")
