"""
(Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore,
the monthly interest rate is After the first month, the value in the account becomes
    100 * (1 + 0.00417) = 100.417

After the second month, the value in the account becomes
    (100 + 100.417) * (1 + 0.00417) = 201.252

After the third month, the value in the account becomes
    (100 + 201.252) * (1 + 0.00417) = 302.507
    and so on.

Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month.
"""

DURATION_IN_MONTH = 6
ANNUAL_INTEREST_RATE = 0.05

monthlyAmount = eval(input("Enter a monthly saving amount: "))

monthlyInterestRate = ANNUAL_INTEREST_RATE/12
totalAccountValue = 0

# first month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)
# 2nd month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)
# 3rd month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)
# 4th month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)
# 5th month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)
# 6th month
totalAccountValue = (monthlyAmount + totalAccountValue) * (1 + 0.00417)

print("After the sixth month, the account value is", int(totalAccountValue*100)/100)

