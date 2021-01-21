# TO GRADER:
# For this portion of the assignment, I have presented two different approaches that ultimately produce the same result.
# The main difference between the two is the method used to get the average change value. They both produce the same number.

# The first (not commented out) is the method I'm most proud because I mostly figured it out myself with the class materials,
# #    and a little help from Google and TA Farshad. It has more sweat equity.
# The method to get the average here will not work if the profit/loss are not distributed chronolically.
# Of course, in this case, they are, so I interpreted the average change as a rate; the net change over time.

# The second (commented out) has some code borrowed from a classmate, Stephanie Richards, and therefore less original. Shout-out to her.
# Her method for finding the average change works both in this case and for when the values aren't a net profit/loss over time.
# Therefore, I wanted to demonstrate that I also took the time to learn that method.

# I'd be curious to find out which way uses less memory. That'd ultimately be the one I'd go with.

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

    # calculate average change over time
    change_average = (last_row-first_row) / (total_months-1)

    # scan through profit/loss list
    for item in range(1,len(profit_loss_list)):

        # make new list of changes between months
        change_list.append(profit_loss_list[item]-profit_loss_list[item-1])

    # add item to change list so it has the same amount of items as table
    change_list.insert(0, int(0))

    # find greatest increase and decrease
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)

    # find increase and decrease month by referencing index of change list
    increase_month = str(months_list[change_list.index(max(change_list))])
    decrease_month = str(months_list[change_list.index(min(change_list))])

print('')
print('Financial Analysis')
print('-------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_rev}')
print(f'Average Change: ${round(change_average, 2)}')
print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

with open(output_path, "w") as text_file:

    print('Financial Analysis', file = text_file)
    print('-------------------------------------------', file = text_file)
    print(f'Total Months: {total_months}', file = text_file)
    print(f'Total: ${total_rev}', file = text_file)
    print(f'Average Change: ${round(change_average, 2)}', file = text_file)
    print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})', file = text_file)
    print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})', file = text_file)

# import os

# import csv

# csvpath = os.path.join('Resources', 'budget_data.csv')

# with open(csvpath) as csvfile:

#     budget = csv.reader(csvfile, delimiter=',')

#     csv_header = next(budget)

#     total_months = 0
#     total_rev = 0
#     change_average = 0
#     profit_loss_list = []
#     months_list = []
#     change_list = []

#     # run through table
#     for row in budget:

#         month_col = str(row[0])
#         profit_loss_col = int(row[1])

#         # make lists out of columns
#         months_list.append(month_col)
#         profit_loss_list.append(profit_loss_col)

#         # add up values of all columns
#         total_rev += profit_loss_col

#     # count rows of table
#     total_months = len(months_list)

#     # run through profit/loss list
#     for item in profit_loss_list:

#         # define previous item in list (previous month)
#         previous_item = profit_loss_list[profit_loss_list.index(item)-1]
#         # calculate change between months
#         change = item - previous_item
#         # make new list out of changes between months
#         change_list.append(int(change))

#     # add item to change list so it has the same amount of items as table
#     change_list.insert(0, int(0))

#     # calculate net change
#     change_sum = sum(change_list)
#     # calculate average change
#     change_average = float(int(change_sum) / (total_months - 1))

#     # find min and max of change
#     greatest_increase = max(change_list)
#     greatest_decrease = min(change_list)

#     # establish index positions in change list
#     increase_list_position = change_list.index(greatest_increase)
#     decrease_list_position = change_list.index(greatest_decrease)

#     # find increase/decrease month using list positions
#     increase_month = months_list[increase_list_position]
#     decrease_month = months_list[decrease_list_position]

# print('Financial Analysis')
# print('-------------------------------------------')
# print(f'Total Months: {total_months}')
# print(f'Total: ${total_rev}')
# print(f'Average Change: ${round(change_average, 2)}')
# print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
# print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

# output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

# with open(output_path, "w") as text_file:

#     print('Financial Analysis', file = text_file)
#     print('-------------------------------------------', file = text_file)
#     print(f'Total Months: {total_months}', file = text_file)
#     print(f'Total: ${total_rev}', file = text_file)
#     print(f'Average Change: ${round(change_average, 2)}', file = text_file)
#     print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})', file = text_file)
#     print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})', file = text_file)