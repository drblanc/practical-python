# pcost.py
#
# Exercise 1.27

total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])

print(f'Total cost {total_cost:0.2f}')
