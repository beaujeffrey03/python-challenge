import os

import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    total_votes = 0
    percent = 0
    winner = 0
    loser = 0
    election_outcome_dict = {}
    candidate_list = []

    for row in csvreader:

        name = row[2]
        total_votes += 1
        count_votes = 0
        
        if name in election_outcome_dict.keys():
            count_votes = count_votes + 1
            # print('yes')

        else:
            election_outcome_dict.update({name: count_votes})
            # print('no')
    
    print('')
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    print(f'{election_outcome_dict}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# Create a dictionary to hold the actor's names.
# actors = {}

# Create a dictionary using the built-in function.
# actors = dict()

# A dictionary of an actor.
# actors = {"name": "Tom Cruise"}
# print(f'{actors["name"]}')

# # Add an actor to the dictionary with the key "name"
# # and the value "Denzel Washington".
# actors["name"] = "Denzel Washington"

# # Print the actors dictionary.
# print(actors["name"])

# # Print only the actor.
# print(f'{actors["name"]}')

# # A list of actors
# actors_list = [
#     "Tom Cruise",
#     "Angelina Jolie",
#     "Kristen Stewart",
#     "Denzel Washington"]

# # Overwrite the value, "Denzel Washington", with the list of actors.
# actors["name"] = actors_list

# # Print the first actor
# print(f'{actors["name"][0]}')
