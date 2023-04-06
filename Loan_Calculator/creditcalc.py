import argparse
from math import log, ceil, floor

# Dm = (P / n) + i * (P - (P*(m - 1)) / n)

parser = argparse.ArgumentParser()
parser.add_argument("--type", required=True, choices=["diff", "annuity"],
                    help="Specify the type of payment: 'annuity' or 'diff'")
parser.add_argument("--principal", type=float, help="The amount of the loan principal")
parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="The loan interest rate")
parser.add_argument("--payment", type=float, help="payment")
args = parser.parse_args()

# calculate differentiated payments
if args.type == "diff":
    if args.payment is None and args.periods > 0 and args.principal > 0 and args.interest > 0:
        p = args.principal
        n = args.periods
        i = (args.interest / 100) / 12
        total = 0
        for m in range(1, n + 1):
            Dm = ceil((p / n) + i * (p - ((p * (m - 1)) / n)))
            total += Dm
            print(f"Month {m}: payment is {ceil(Dm)}")
        print(f"Overpayment = {int((total - p))}")
    else:
        print("Incorrect parameters.")

# calculate annuity payments
if args.type == "annuity":
    if args.payment is None:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            p = args.principal
            n = args.periods
            i = (args.interest / 100) / 12
            # p_m=args.payment

            an_p = ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
            overpayment = (an_p * n) -p
            print(f"Your annuity payment = {an_p}!")
            print(f"Overpayment = {ceil(overpayment)}")
        else:
            print("Incorrect parameters.")

    elif args.principal is None: # and args.payment > 0 and args.periods > 0 and args.interest > 0
        # p = args.principal
        n = args.periods
        i = (args.interest / 100) / 12
        p_m = args.payment

        total = n * p_m
        p = p_m * ((1 - (1 + i) ** (-n)) / i)
        print(f"Your loan principal = {floor(p)}!")
        print(f"Overpayment = {ceil(total - p)}")

    elif args.periods is None:
        if args.principal and args.payment and args.interest:
            p = args.principal
            # n = args.periods
            i = (args.interest / 100) / 12
            p_m = args.payment

            n = ceil(log(p_m / (p_m - (i * p)), 1 + i))
            total = n * p_m
            months = ceil(n % 12)
            years = ceil(n // 12)
            if months == 12:
                years += 1
                months = 0
            # Output the result
            year_str = f"{years} year{'s' if years > 1 else ''}" if years > 0 else ""
            month_str = f"{months} month{'s' if months > 1 else ''}" if months > 0 else ""
            print(f"It will take {year_str} {month_str} to repay this loan!")
            print(f"Overpayment = {ceil(total - p)}")
        else:
            print("Incorrect parameters.")
