import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--principal", type=float)

args = parser.parse_args()

count_variables = ((args.payment is None) + (args.periods is None) +
                   (args.interest is None) + (args.principal is None) +
                   (args.type is None))

if count_variables == 1:
    if args.type != 'diff' and args.type != 'annuity':
        print('Incorrect parameters')
    elif args.type == 'diff':
        if not (args.payment is None):
            print('Incorrect parameters')
        else:
            interest = args.interest / 1200
            total = 0
            for m in range(1, args.periods + 1):
                payment = math.ceil(args.principal / args.periods +
                                    interest * (args.principal -
                                                args.principal * (m - 1) / args.periods))
                total += payment
                print(f'Month {m}: paid out {payment}')
            print()
            print(f'Overpayment = {int(total - args.principal)}')
    elif args.type == 'annuity':
        interest = args.interest / 1200
        if args.periods is None:
            months = math.ceil(math.log(args.payment / (args.payment - interest * args.principal), 1 + interest))
            if months % 12 == 0:
                if months == 12:
                    text_year = 'year'
                else:
                    text_year = 'years'
                print(f'You need {months // 12} {text_year} to repay this credit')
                print(f'Overpayment = {int(months * args.payment - args.principal)}')
            elif months < 12:
                if months == 1:
                    text_month = 'month'
                else:
                    text_month = 'months'
                print(f'You need {months} {text_month} to repay this credit')
                print(f'Overpayment = {int(months * args.payment - args.principal)}')
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
                print(f'Overpayment = {int(months * args.payment - args.principal)}')
        elif args.payment is None:
            annuity = math.ceil(args.principal * ((interest * (1 + interest) ** args.periods) / ((1 + interest) ** args.periods - 1)))
            print(f'Your annuity payment = {annuity}!')
            print(f'Overpayment = {int(annuity * args.periods - args.principal)}')
        elif args.principal is None:
            principal = math.ceil(args.payment / ((interest * (1 + interest) ** args.periods) / ((1 + interest) ** args.periods - 1)))
            print(f'Your principal = {principal}!')
            print(f'Overpayment = {int(args.payment * args.periods - principal)}')
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
