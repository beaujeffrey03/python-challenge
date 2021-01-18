import os

import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    total_votes = 0
    candidate_list = []
    candidate_vote_list = []
    count_votes = 0
    candidate_name = 0
    county = []
    percent_votes = 0
    winner = 0
    loser = 0

    for row in csvreader:

        candidate_col = row[2]

        total_votes += 1

        if candidate_col not in candidate_list:
            candidate_list.append(candidate_col)

        # if candidate_name in candidate_list:
        #     candidate_vote_list = candidate_vote_list.append(candidate_vote_list + 1)

    # print('')
    # print(f'{candidate_vote_list}')
    print('')
    print(f'{candidate_list}')
    print('')
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    print(f'{candidate_name}: {percent_votes} ({count_votes})')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')