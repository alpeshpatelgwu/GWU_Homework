import os
import csv
import pandas as pd 

#electionpath = os.path.join('..', 'resources', 'election_data.csv')

print("This is HW Assignment #3 to analyze Election Data")
print("")


# Create a variable that holds the import of the election_data CSV File
electionpath = "C:\\Users\\aipat\\python-challenge\\resources\\election_data.csv"

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

voter_id = []
county = []
candidates = []
total_votes_casted = 0
khan_votes_casted = 0
correy_votes_casted = 0
li_votes_casted = 0
otooley_votes_casted = 0
election_winner = 0
candidate_list = []
candidate_votes = []


with open(electionpath, 'r') as electionfile:
    electionreader = csv.reader(electionfile, delimiter=",")
    electionheader = next(electionreader)
    
  
    #this will iterate through each row of the csv file and read it
    #this for loop will continue to loop through the csvfile till 
    #it reaches the end
    # === What do you want to do in this loop? ===
	
    for row in electionreader:
       
        #this will store the values of each column in either voter_id, county, or candidate list
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    # iterate through to candidate 
	# Candidate names Khan / Correy / Li / O'Tooley
	
    for candidatevotes in candidates:
        total_votes_casted = total_votes_casted + 1
        if candidatevotes == "Khan":
            khan_votes_casted = khan_votes_casted + 1
        elif candidatevotes == "Correy":
            correy_votes_casted = correy_votes_casted + 1
        elif candidatevotes == "Li":
            li_votes_casted = li_votes_casted + 1
        elif candidatevotes == "O'Tooley":
            otooley_votes_casted = otooley_votes_casted + 1

candidate_list = ['Khan', 'Correy', 'Li', 'O Tooley']
candidate_votes = [khan_votes_casted, correy_votes_casted, li_votes_casted, otooley_votes_casted]

results_dict = dict(zip(candidate_list, candidate_votes))
max_value = max(results_dict.values())
elected = [key for key, value in results_dict.items() if value == max_value]

khan_percent = khan_votes_casted / total_votes_casted
correy_percent = correy_votes_casted / total_votes_casted
li_percent = li_votes_casted / total_votes_casted
otolley_percent = otooley_votes_casted / total_votes_casted

print("============================================================")
print("")
print(f'There are a total of {total_votes_casted} votes casted')
print(f'Candidate Khan has {khan_percent:.2%} of votes with {khan_votes_casted} votes casted')
print(f'Candidate Correy has {correy_percent:.2%} of votes with {correy_votes_casted} votes casted')
print(f'Candidate Li has {li_percent:.2%} of votes with {li_votes_casted} votes casted')	
print(f'Candidate O Tooley has {otolley_percent:.2%} of votes with {otooley_votes_casted} votes casted')
print(f'These are the results of the election {results_dict}')
print(f'The winner is {elected} with {max_value} votes!')				
print("")
print("This is the end of Election Analysis")
print("============================================================")

output_electionresults = "C:\\Users\\aipat\\python-challenge\\PyPoll\\PyPoll_ElectionResults.txt"

with open(output_electionresults, 'w') as electionfile:
    
    electionfile.write("============================================================")
    electionfile.write("\n")
    electionfile.write("These are the results of this year's election")
    electionfile.write("\n")
    electionfile.write(f'There are a total of {total_votes_casted} votes casted')
    electionfile.write("\n")	
    electionfile.write(f'Candidate Khan has {khan_percent:.2%} of votes with {khan_votes_casted} votes casted')
    electionfile.write("\n")	
    electionfile.write(f'Candidate Correy has {correy_percent:.2%} of votes with {correy_votes_casted} votes casted')
    electionfile.write("\n")	
    electionfile.write(f'Candidate O Tooley has {otolley_percent:.2%} of votes with {otooley_votes_casted} votes casted')
    electionfile.write("\n")	
    electionfile.write(f'These are the results of the election {results_dict}')
    electionfile.write("\n")	
    electionfile.write(f'The winner is {elected} with {max_value} votes!')
    electionfile.write("\n")	
    electionfile.write("This is the end of Election Analysis")
    electionfile.write("\n")
    electionfile.write("============================================================")
	