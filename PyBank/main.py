# TO GRADER:
# For this portion of the code, I have presented two different approaches that ultimately produce the same result.
# The main difference between the two is the method used to get the average change value. They both produce the same number.

# The first (not commented out) is the method I'm most proud because I mostly figured it out myself with the class materials
# #    and a little help from Google.
# The method to get the average will not work if the profit/loss are not distributed chronolically.
# Of course, in this case, they are, so I interpreted the average change as a rate. The amount of change over time.

# The second (commented out) has some code borrowed from a classmate, Stephanie Richards, and therefore less original.
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

    for row in budget:

        month_col = str(row[0])
        profit_loss_col = int(row[1])

        total_months += 1
        profit_loss_list.append(profit_loss_col)
        months_list.append(month_col)

        total_rev += profit_loss_col

        if total_months == 1:
            first_row = profit_loss_col
        
        else:
            last_row = profit_loss_col

    change_average = (last_row - first_row) / (total_months - 1)

    for item in range(1,len(profit_loss_list)):

        change_list.append(profit_loss_list[item] - profit_loss_list[item - 1])

    change_list.pop(0)
    change_list.insert(0, int(0))

    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)

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

#     for row in budget:

#         month_col = str(row[0])
#         profit_loss_col = int(row[1])

#         months_list.append(month_col)
#         profit_loss_list.append(profit_loss_col)

#         monthly_change = int(profit_loss_col)

#         total_rev = total_rev + monthly_change

#     total_months = len(months_list)

#     change_list = []
#     for item in profit_loss_list:

#         previous_item = profit_loss_list[profit_loss_list.index(item)-1]
#         change = item - previous_item
#         change_list.append(int(change))

    # change_list.pop(0)
    # change_list.insert(0, int(0))

#     change_sum = sum(change_list)
#     change_average = float(int(change_sum) / (total_months - 1))

#     greatest_increase = max(change_list)
#     greatest_decrease = min(change_list)

#     increase_list_position = change_list.index(greatest_increase)
#     decrease_list_position = change_list.index(greatest_decrease)

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