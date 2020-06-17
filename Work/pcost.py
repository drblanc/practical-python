# pcost.py
#
# Exercise 1.33

import sys
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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

