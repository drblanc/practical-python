# mortgage.py
#
# Exercise 1.7

principal = 500000.00
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 1
extra_payment_start_month = 49 # first extra payment in year 5
extra_payment_end_month = 49+48-1 # last extra payment 48 months later
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate/12)
    if principal < payment:
        payment = principal
    principal = principal - payment
    if extra_payment_start_month <= month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    total_paid = total_paid + payment
    print(f'{month:3d} {total_paid:9.2f} {principal:9.2f}')
    month += 1

print(f'Total paid {total_paid:0.2f}')

