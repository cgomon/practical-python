# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    cost = 0

    f = open(filename, 'rt')
    next(f)
    for line in f:
        line = line.strip('\n')
        row = line.split(',')
        try:
            cost += int(row[1]) * float(row[2])
        except ValueError:
            print('''Couldn't parse''', row)
                  
    f.close()
    return cost

cost = portfolio_cost('C:/Users/cgomo/Documents/GitHub/practical-python/Work/Data/portfolio.csv')
print(f'Total cost {cost:0.2f}')

cost = portfolio_cost('C:/Users/cgomo/Documents/GitHub/practical-python/Work/Data/missing.csv')
print(f'Total cost {cost:0.2f}')