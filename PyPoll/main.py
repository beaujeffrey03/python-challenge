# Thanks to classmate Melissa Lowe for collaborating with me on this one.

import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    election = csv.reader(csvfile, delimiter=',')

    csv_header = next(election)

    total_votes = 0
    winner = 0
    all_votes_list = []

    # run through table
    for row in election:

        # make list out of candidate name column
        candidate = row[2]
        all_votes_list.append(candidate)
        # count rows as total votes
        total_votes += 1

    # make list of unique candidates
    candidates_list = []
    for name in all_votes_list:
        if name not in candidates_list:
            candidates_list.append(name)

    # compare list of unique candidates to all rows in candidate column, count occurrences of each candidate
    votes_list = []
    vote_tally = 0
    for name in candidates_list:
        for vote in all_votes_list:
            if vote == name:
                vote_tally = int(vote_tally) + 1
            
        # make new list with total votes per candidate
        votes_list.append(vote_tally)
        # reset vote count after each candidate
        vote_tally = 0

    # make list to hold percentages for each candidate
    percent_list = []
    for each in votes_list:
        vote_percent = round(float((int(each) / (total_votes))*100),2)
        percent_format = "{:.2f}".format(vote_percent)
        percent_list.append(percent_format)

    # put the three lists into tuple for easy printing
    results_tuple = tuple(zip(candidates_list, percent_list, votes_list))

    # find most votes from votes list
    winner_vote = max(votes_list)
    # determine index of winner votes in votes list
    winner_index = votes_list.index(winner_vote)
    # apply index from votes list to candidate list
    winner = candidates_list[winner_index]

output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(output_path, "w") as text_file:

    print('Election Results', file = text_file)
    print('--------------------------------', file = text_file)
    print(f'Total Votes: {total_votes}', file = text_file)
    print('--------------------------------', file = text_file)
    for result in results_tuple:
        print(f'{result[0]}: {result[1]}% ({result[2]})', file = text_file)
    print('--------------------------------', file = text_file)
    print(f'Winner: {winner}', file = text_file)
    print('--------------------------------', file = text_file)