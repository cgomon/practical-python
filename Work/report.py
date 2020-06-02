# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 
                       'shares': int(row[1]), 
                       'price': float(row[2])}
            portfolio.append(holding)
    
    return portfolio

def read_portfolio_lc(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, int, float]
        portfolio = [[f(val) for f, val in zip(types, row)] for row in rows]
        return portfolio
        
def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])
    
    return prices

def compute_pnl(portfolio, prices):
    init_value = 0
    current_value = 0
    pnl = 0
    for holding in portfolio:
        mark = prices[holding['name']]
        open_px = holding['price']
        pos = holding['shares']
        init_value += pos * open_px
        current_value += pos * mark
        pnl += pos * (mark - open_px)
        
    print(f'Initial Portfolio Value: {init_value:0.2f}')
    print(f'Current Portfolio Value: {current_value:0.2f}')
    print(f'Current PnL: {pnl:0.2f}')
    return [init_value, current_value, pnl]

def make_report(portfolio, prices):
    rpt = []
    headers = ('Name', 'Shares', 'Price', 'Change')
    sep = '-' * 10
    sep_row = (sep + ' ') * 3 + sep
    
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{sep_row}')
    
    for holding in portfolio:
        ticker = holding['name']
        pos = holding['shares']
        mark = prices[ticker]
        change = mark - holding['price']
        rpt.append((ticker, pos, mark, change))
        print(f'{ticker:>10s} {pos:>10d} {mark:>10.2f} {change:>10.2f}')
    
    return rpt
        