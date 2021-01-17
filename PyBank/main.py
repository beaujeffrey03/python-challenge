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
    monthly_change = []
    greatest_increase = 0
    month_increase = 0
    greatest_decrease = 0
    month_decrease = 0

    for row in csvreader:

        month_col = str(row[0])
        profit_loss_col = int(row[1])

        total_months += 1

        total += profit_loss_col

        if total_months == 1:
            first_row = profit_loss_col
        
        else:
            last_row = profit_loss_col

        # if profit_loss_col >= monthly_change:
        #     greatest_increase = profit_loss_col

        # if profit_loss_col == greatest_increase:
        #     month_increase = month_col

        # elif profit_loss_col == greatest_decrease:
        #     month_decrease = month_col

average_change = (last_row - first_row) / (total_months - 1)

average_change = round(float(average_change), 2)

print('')
print('Financial Analysis')
print('-------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})')