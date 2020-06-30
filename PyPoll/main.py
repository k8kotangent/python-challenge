# '''
#     1. total number of votes cast: done
#     2. complete list of candidates who received votes
#     3. percentage of votes each candidate won
#     4. total number of votes each candidate won
#     5. winne fo the election based on pop vote

#     "list: voterID, list1: County, list2:candidate
# '''
import csv
import os
f=open('Analysis\PyPoll_analysis.txt', 'w')

csvpath= os.path.join("Resources", "election_data.csv")

county = []
candidate=[]
candidate_count ={}
candidate_percentage=[]

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    voter=0
    for row in csvreader:
        voter += int(1)
        candidate.append(row[2])
    
    from collections import Counter
    candidate_count = Counter(candidate)
    

    print('Election Results')   
    print('----------------------')
    print(f'Total Votes: {voter}')
    print('----------------------')
    f.write(f'Election Results\n----------------------\nTotal Votes: {voter}\n----------------------')
    f.write('\n')
    wordList =list(candidate_count.keys())
    for key in wordList:
        candidate_percentage=((candidate_count[key])/voter)*100
        max_key=max(candidate_count, key=candidate_count.get)
        format_candidate_percentage=format(candidate_percentage, ".3f")
        print(f'{key}: {format_candidate_percentage}% ({candidate_count[key]})')
        f.write(f'{key}: {format_candidate_percentage}% ({candidate_count[key]}')
        f.write('\n')
    print('----------------------')
    print(f'Winner: {max_key}')
    f.write(f'----------------------\nWinner: {max_key}')
f.close()
    
   