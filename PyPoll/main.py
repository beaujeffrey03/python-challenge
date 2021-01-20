import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

def percent_func(dict):
    total = 0
    for count in dict:
        total = total + dict[count]
    for percent in dict:
        dict[percent] = (float((dict[percent])/total)) * 100
    return dict

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    total_votes = 0
    winner = 0
    votes_dict = {}
    percent_dict = {}

    for row in csvreader:

        name = row[2]
        total_votes += 1
        votes = {}

        if name not in votes_dict:
            votes_dict[name] = 1

        else:
            votes_dict[name] += 1

    percent_dict = percent_func(votes_dict)

    print('')
    print (votes_dict)
    print('')
    print (percent_dict)

    
    print('')
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    print(f'{percent_dict}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')