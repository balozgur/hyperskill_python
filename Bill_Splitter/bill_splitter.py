# write your code here
import random

print("Enter the number of friends joining (including you):")
n = int(input())
if n == 0 or n < 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    f_dict = dict()
    for i in range(1, n + 1):
        name = input()
        f_dict[name] = 0
    print("Enter the total bill value:")
    bill = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = (input()).lower()
    if lucky == "no":
        print("No one is going to be lucky")
        for key in f_dict.keys():
            f_dict[key] = round(bill / n, 2)
        print(f_dict)
    if lucky == "yes":
        l_ = random.choice(list(f_dict.keys()))
        print(f"{l_} is the lucky one!")
        for key in f_dict.keys():
            if key == l_:
                pass
            else:
                f_dict[key] = round(bill / (n - 1), 2)
        print(f_dict)