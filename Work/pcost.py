# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
	f = open(filename, 'rt')
	headers = next(f)
	rows = csv.reader(f)
	total_cost = 0

	for data_row in rows:
		try:
			num_stocks = int(data_row[1])
			price = float(data_row[2])
			total_cost = total_cost + num_stocks*price
		except ValueError:
			print("Missing value. Skip the stocks for", data_row[0])
	f.close()
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)



