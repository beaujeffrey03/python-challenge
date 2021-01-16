import os

import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_votes = 0
    candidate_name = 0
    percent_votes = 0
    count_votes = 0
    winner = 0
    loser = 0

    for row in csvreader:

        total_votes += 1


    print('')
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    print(f'{candidate_name}: {percent_votes} ({count_votes})')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')