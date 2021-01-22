# TO GRADER:
# Props to classmate Stephanie Richards for posting her code.
# I got a little tripped up with calculating average change and her technique for creating lists from the rows really opened
# things up for me.

import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    budget = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget)

    total_months = 0
    total_rev = 0
    change_average = 0
    change_list = []
    profit_loss_list = []
    months_list = []

    # run through table
    for row in budget:

        month_col = str(row[0])
        profit_loss_col = int(row[1])

        # count rows in table
        total_months += 1

        # make list out of profit/loss column
        profit_loss_list.append(profit_loss_col)
        # make list out of month column
        months_list.append(month_col)

        # get total revenue by adding to total at each row
        total_rev += profit_loss_col

        # store first row
        if total_months == 1:
            first_row = profit_loss_col
        
        # store last row
        else:
            last_row = profit_loss_col

    # scan through profit/loss list
    for item in range(1,len(profit_loss_list)):

        # make new list of changes between months
        change_list.append(profit_loss_list[item]-profit_loss_list[item-1])

    # calculate net change
    net_change = sum(change_list)
    # calculate average change
    change_average = net_change/len(change_list)

    # add item to change list so it has the same amount of items as table
    change_list.insert(0, int(0))

    # find greatest increase and decrease
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)

    # find increase and decrease month by referencing index of change list
    increase_month = str(months_list[change_list.index(max(change_list))])
    decrease_month = str(months_list[change_list.index(min(change_list))])

output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

with open(output_path, "w") as text_file:

    print('Financial Analysis\n'
    f'------------------------------------------- \n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_rev}\n'
    f'Average Change: ${round(change_average, 2)}\n'
    f'Greatest Increase in Profits: {increase_month} (${greatest_increase})\n'
    f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})', file = text_file)