income = int(input())
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
else:
    percent = 28

print('The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.format(income=income,
                                                                                     percent=percent,
                                                                                     calculated_tax=round(income * percent / 100)))
