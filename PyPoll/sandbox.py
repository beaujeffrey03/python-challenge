import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')
​
with open(csvpath) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    #print(election_data)
   
    #Count the number of rows in the data set, minus the header
    header = next(election_data)
    #print(header)
​
    #define values
    voter_ID = []
    county = []
    candidate_name = []
​
    #begin for loop
    for row in election_data:
​
        #add data to lists
        voter_ID.append(str(row[0]))
        county.append(str(row[1]))
        candidate_name.append(str(row[2]))
    #print(voter_ID)
​
# Calcualte the total number of votes cast
total_votes = len(voter_ID)
#print(total_votes)
​
#Get unique values from list and write to new list:
#geeksforgeeks.org/python-get-unique-values-list/
# function to get unique values 
​
unique_candidates = []
candidate_votes = []
vote_total = 0
def unique(candidate_name): 
  
    # traverse for all elements 
    for name in candidate_name: 
        # check if exists in unique_list or not 
        if name not in unique_candidates: 
            unique_candidates.append(name) 
    # print list 
    #for name in unique_candidates: 
        #print (name)
    return unique_candidates    
​
unique(candidate_name)
#print(unique_candidates)
​
#count votes per candidate 
candidate_votes = []
def vote_count(unique_candidates):
    #set initial counter
    vote_total = 0
    #traverse first list
    for name in unique_candidates:
        #compare to second list
        for vote in candidate_name:
            #add votes
            if name == vote:
                vote_total = int(vote_total) + 1
        #add to list
        candidate_votes.append(vote_total)
        #print(candidate_votes)
        #reset counter
        vote_total = 0
    return candidate_votes
​
vote_count(unique_candidates)
#print(candidate_votes)
​
#find winner
win_vote = max(candidate_votes)
win_index = candidate_votes.index(win_vote)
winner = unique_candidates[win_index]
#print(winner)
​
​
#calcualte vote percentage total
candidate_vote_percent = []
for x in (candidate_votes):
    vote_percent = round((float(int(x) / int(total_votes)) * 100), 3)
    candidate_vote_percent.append(vote_percent)
#print(candidate_vote_percent)
​
#print(unique_candidates)
#print(candidate_vote_percent)
#print(candidate_votes)
​
#zip lists to make tuple
candidate_tuple = tuple(zip(unique_candidates, candidate_vote_percent, candidate_votes))
​
#candidate_1 = list(candidate_tuple[0])
#print(candidate_1)
​
print(" ")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for lst in candidate_tuple:
    print(f"{lst[0]}: {lst[1]}00% ({lst[2]})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
​
#Open export path for text file:
#tip o' the pin to this exchange: 
# https://stackoverflow.com/questions/5214578/print-string-to-text-file
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")
​
with open(output_path, "w") as text_file:
​
    print("Election Results", file = text_file)
    print("--------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("--------------------------", file = text_file)
    for lst in candidate_tuple:
        print(f"{lst[0]}: {lst[1]}00% ({lst[2]})", file=text_file)
    print("--------------------------", file = text_file)
    print(f"Winner: {winner}", file = text_file)
    print("--------------------------", file = text_file)