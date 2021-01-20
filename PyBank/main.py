import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    total_months = 0
    total = 0
    average_change = 0
    revenue = []
    revenue_change = []
    month = []
    total_revenue = 0
    max_profit = 0
    month_max = ""
    min_profit = 0
    month_min = ""

    for row in csvreader:

        month_col = str(row[0])
        profit_loss_col = int(row[1])

        total_months += 1
        total_revenue += profit_loss_col
        revenue.append(profit_loss_col)
        month.append(month_col)

        total += profit_loss_col

        if total_months == 1:
            first_row = profit_loss_col
        
        else:
            last_row = profit_loss_col

        for item in range(1,len(revenue)):

            revenue_change.append(revenue[item] - revenue[item - 1])

            max_profit = max(revenue_change)
            min_profit = min(revenue_change)

            month_max = str(month[revenue_change.index(max(revenue_change))])
            month_min = str(month[revenue_change.index(min(revenue_change))])

average_change = (last_row - first_row) / (total_months - 1)

print('')
print('Financial Analysis')
print('-------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {month_max} (${max_profit})')
print(f'Greatest Decrease in Profits: {month_min} (${min_profit})')