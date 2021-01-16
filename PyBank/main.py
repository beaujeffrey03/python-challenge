import os

import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    total_months = 0
    total = 0
    average_change = 0
    monthly_change = 0
    month_increase = 0
    greatest_increase = 0
    month_decrease = 0
    greatest_decrease = 0

    for row in csvreader:

        month_col = str(row[0])
        profit_loss_col = int(row[1])

        total_months += 1

        total += profit_loss_col

        # average_change = (first_row - last_row) / (total_months - 1)

    for row in enumerate(csvreader):

        print(row)

    print('')
    print('Financial Analysis')
    print('--------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {month_increase} ({greatest_increase})')
    print(f'Greatest Decrease in Profits: {month_decrease} ({greatest_decrease})')