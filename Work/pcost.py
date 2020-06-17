# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                nshares = int(row[1])
                sharecost = float(row[2])
            except ValueError:
                print('Cannot parse:', line)
                nshares = 0
            total_cost = total_cost + nshares * sharecost
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

