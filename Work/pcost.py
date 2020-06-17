# pcost.py
#
# Exercise 1.32

import csv

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename)
    rows = csv.reader(f)

    headers = next(rows)
    for row in rows:
        try:
            nshares = int(row[1])
            sharecost = float(row[2])
        except ValueError:
            print('Cannot parse:', row)
            nshares = 0
        total_cost = total_cost + nshares * sharecost

    f.close()
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

