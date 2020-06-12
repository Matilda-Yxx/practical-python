# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            holding = {
                'name': name,
                'shares': nshares,
                'price': price
            }
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    ''' Read prices from a csv file into a dictionary.
    Key would be the name of the stock, value is the price of the stock.'''
    portfolio = {}

    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            portfolio[row[0]] = float(row[1])
        except:
            print('Cannot extract price information for the row.')
    f.close()
    return portfolio

def make_report(portfolio, price):
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price_in = stock['price']
        try:
            price_out = price[name]
            price_change = price_out - price_in
        except:
            print('Cannot find the current stock price.')
        report.append((name, shares, f'${price_out:.2f}', price_change))

    return report




# compute total gain/loss
gain = 0.0
portfolio = read_portfolio('Data/portfolio.csv')
price = read_prices('Data/prices.csv')

for p in portfolio:
    shares = p['shares']
    price_in = p['price']

    name = p['name']
    try:
        price_out = price[name]
    except:
        print('Cannot find the current stock price.')

    gain += shares * (price_out-price_in)

print('Gain/loss is given by: ', gain)

report = make_report(portfolio, price)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
divider = '----------'
print(f'{divider:>10s} {divider:>10s} {divider:>10s} {divider:>10s}')
for r in report:
    print('%10s %10d %10s %10.2f' % r)







