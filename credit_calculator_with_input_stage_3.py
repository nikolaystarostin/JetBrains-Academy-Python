import math

param = input('''What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:
''')
if param == 'n':
    principal = float(input('Enter credit principal: '))
    payment = float(input('Enter monthly payment: '))
    interest = float(input('Enter credit interest: ')) / 1200
    months = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    if months % 12 == 0:
        if months == 12:
            text_year = 'year'
        else:
            text_year = 'years'
        print(f'You need {months // 12} {text_year} to repay this credit')
    elif months < 12:
        if months == 1:
            text_month = 'month'
        else:
            text_month = 'months'
        print(f'You need {months} {text_month} to repay this credit')
    else:
        if months // 12 == 1:
            text_year = 'year'
        else:
            text_year = 'years'
        if months % 12 == 1:
            text_month = 'month'
        else:
            text_month = 'months'
        print(f'You need {months // 12} {text_year} and {months % 12} {text_month} to repay this credit')
if param == 'a':
    principal = float(input('Enter credit principal: '))
    periods = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: ')) / 1200

    annuity = math.ceil(principal * ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))

    print(f'Your annuity payment = {annuity}!')

elif param == 'p':
    payment = float(input('Enter monthly payment: '))
    periods = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: ')) / 1200

    principal = math.ceil(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))

    print(f'Your principal = {principal}!')
