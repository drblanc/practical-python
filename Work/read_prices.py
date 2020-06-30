# Exercise 2.6

import csv

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

