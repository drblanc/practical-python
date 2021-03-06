# report.py
#
# Exercise 2.4-2.7

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            portfolio.append({'name':row[0], 'shares':nshares, 'price':price})
    return portfolio

def read_prices(filename):
    '''Reads csv of name,price into a dict'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price = float(row[1])
                prices[row[0]] = price
            except:
                pass
    return prices

def make_report(stocklist, pricelist):
    report = []
    for h in stocklist:
        name = h['name']
        report.append((name, h['shares'], pricelist[name],
            pricelist[name]-h['price']))
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('%10s %10s %10s %10s' % (('-'*10,)*4))
for n, s, p, c in report:
    print('%10s %10d %10s %10.2f' % (n, s, '$%.2f' % p, c))

