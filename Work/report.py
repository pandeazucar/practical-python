# report.py
#
# Exercise 2.4

import csv
import sys

# Enter portfolio filename
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = input("Please enter a filename: ")


def main():
    """
    This script is meant to be executed at the terminal. Given a list of stocks and
    a dictionary of current stock prices, it computes the current loss/gain of
    the user's stocks. It also prints out a table showing the loss/gain.
    """
    portfolio = read_portfolio(url)
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    headers = ['Name', 'Shares', 'Price', 'Change']

    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    for s in headers:
        print(f"{'':->10s}", end=' ')

    print("")

    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def read_portfolio(filename):
    """
    Reads a csv file where the user's stocks are clearly defined
    based on a structure of name, shares, price
    """
    # define empty portfolio which is the variable that's going to return
    portfolio = []
    # read the file and save each row like a tuple, then add it to the portfolio
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            # stock = (row[0], int(row[1]), float(row[2]))
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    """
    Reads a file detailing the current prices of stocks.
    The program will open and read from the file and create a structured
    dictionary, which will be used as input for the loss/gain calculations.
    """
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
    """
    This function computes the loss/gain of each stock based on current
    prices, and also prints a formatted and user-friendly table
    showing the data.
    """
    # Output needs to be a list of tuple containing: name, shares, price, change
    report_rows = []
    for stock in stocks:
        diff = round(prices[stock['name']] - stock['price'], 2)
        report_rows.append((stock['name'], stock['shares'],
                            prices[stock['name']], diff))

    return report_rows


if __name__ == "__main__":
    main()
