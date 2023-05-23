# report.py
#
# Exercise 2.4

import csv


def main():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    headers = ['Name', 'Shares', 'Price', 'Change']

    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    for s in headers:
        print(f"{'':->10s}", end=' ')

    print("")

    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {'$':>s}{price:>10.2f} {change:>10.2f}")


def read_portfolio(filename):
    # define empty portfolio which is the variable that's going to return
    portfolio = []
    # read the file and save each row like a tuple, then add it to the portfolio
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            # stock = (row[0], int(row[1]), float(row[2]))
            stock = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2])
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    # We are going to use an empty dictionary to insert stock values
    prices = {}

    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue

    return prices


def make_report(stocks, prices):
    # Output needs to be a list of tuple containing: name, shares, price, change
    report_rows = []
    for stock in stocks:
        diff = round(prices[stock['name']] - stock['price'], 2)
        report_rows.append((stock['name'], stock['shares'],
                            prices[stock['name']], diff))

    return report_rows


if __name__ == "__main__":
    main()

# Compute gain/loss of current stocks
'''
pf = read_portfolio('Data/portfolio.csv')
current_prices = read_prices('Data/prices.csv')
total = 0.0
for s in pf:
    total += int(s['shares']) * float(s['price'])

current_value = 0.0
for item in pf:
    current_value += item['shares'] * current_prices[item['name']]

difference = current_value - total
if difference > 0:
    print(f"You have a gain of ${difference:,.2f}")
elif difference < 0:
    print(f"You have a loss of ${difference:,.2f}")
else:
    print("Your stock portfolio is valued the same as yesterday")
'''
