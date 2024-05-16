import os
import csv
#establishing path to resources folder and csv data file 

election_csv = os.path.join("Resources","election_data.csv")
analysis_txt = os.path.join("analysis","PyPoll_results.txt")

total_votes = 0

#total number of votes each candidate won
vote_count = 0
#The winner of the election
winning_cand = ""

print("Election Results")
print("-------------------------")

with open(election_csv, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    #converting csv file into list for reading through
    votes_data = list(csv_reader)
    #list of candidates who received votes
    candidates = {}
    #total = length of the entire file after skipped header
    total_votes = len(votes_data)
    for row in votes_data:
        #storing unique candidate name as 1, whereas if already a key then increment
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

    print(f"Total Votes: {total_votes}") 
    print("-------------------------")
    #looping through each item in candidates list, calculating and printing percentage and vote count
    for candidate, vote_count in candidates.items():
        percent = (vote_count / total_votes) * 100
        print(f'{candidate}: {percent:.3f}% ({vote_count})')

winning_cand = max(candidates, key = candidates.get)
print("-------------------------")
print(f'Winner: {winning_cand}')

print("-------------------------")

#writing into text file results
with open(analysis_txt, 'a') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, vote_count in candidates.items():
        percent = (vote_count / total_votes) * 100
        f.write(f'{candidate}: {percent:.3f}% ({vote_count})\n')
    f.write("-------------------------\n")
    f.write(f'Winner: {winning_cand}\n')
    f.write("-------------------------\n")
