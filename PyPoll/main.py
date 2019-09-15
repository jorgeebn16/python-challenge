## PyPoll

# Dependencies
import os
import csv

# file input
PyPoll = os.path.join("Resources","election_data.csv")

# Variables & Counters
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
total_count = []

with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y*100)/count
        vote_percent.append(z)
        # print(z)
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    total_count = "{:,}".format(count)
    # print(total_count)
 
# Terminal Results 
print("----------------------------------------------------------")
print("Election Results")   
print("----------------------------------------------------------")
print("Total participation:" + str(total_count))
print("----------------------------------------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("----------------------------------------------------------")
print("The winner is: " + winner)
print("----------------------------------------------------------")

# Text File Results
with open('election_results.txt', 'w') as text:
    text.write("Election Results")
    text.write("----------------------------------------------------------")
    text.write("Total Participation: " + str(count))
    text.write("----------------------------------------------------------")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")")
    text.write("----------------------------------------------------------")
    text.write("The winner is: " + winner )
    text.write("----------------------------------------------------------")