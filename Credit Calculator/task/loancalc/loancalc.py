import math
import argparse

parser = argparse.ArgumentParser(description='Loan calculator')

parser.add_argument('--type', type=str, help='the type')
parser.add_argument('--payment', type=int, help='the payment')
parser.add_argument('--principal', type=int, help='the principal')
parser.add_argument('--periods', type=int, help='number of periods')
parser.add_argument('--interest', type=float, help='interest')

args = parser.parse_args()


def print_error():
    print('Incorrect parameters')


if args.type not in ['annuity', 'diff'] or args.type is None:
    print_error()
    exit()

if args.type == 'diff':
    if args.payment is not None:
        print_error()
        exit()

    P = args.principal
    n = args.periods
    i = args.interest / 12 / 100
    S = 0

    for p in range(1, n + 1):
        d = math.ceil(P / n + i * (P - P * (p - 1) / n))
        print('Month {month}: payment is {payment}'.format(month=p, payment=d))
        S += d

    print('\nOverpayment = {over}'.format(over=int(S - P)))
elif args.type == 'annuity':
    if args.interest is None:
        print_error()
        exit()
    elif args.periods is None:
        P = args.principal
        A = args.payment
        i = args.interest / 12 / 100

        n = math.ceil(math.log(A / (A - i * P), 1 + i))

        print('It will take {periods} years to repay this loan!'.format(periods=int(n / 12)))
        print('Overpayment = {over}'.format(over=n * A - P))
    elif args.principal is not None:
        P = args.principal
        n = args.periods
        i = args.interest / 12 / 100

        A = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

        print('Your annuity payment = {payment}!'.format(payment=A))
        print('Overpayment = {over}'.format(over=math.ceil(n * A - P)))
    elif args.payment is not None:
        A = args.payment
        n = args.periods
        i = args.interest / 12 / 100

        P = int(A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))

        print('Your loan principal = {principal}!'.format(principal=P))
        print('Overpayment = {over}'.format(over=A * n - P))

if args.type is None:
    print_error()
    exit()

if (args.payment and args.payment < 0) \
        or (args.principal and args.principal < 0) \
        or (args.periods and args.periods < 0)\
        or (args.interest and args.interest < 0):
    print_error()
    exit()

