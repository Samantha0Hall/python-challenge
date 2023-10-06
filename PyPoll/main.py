import os
import csv

#Set Path
csvpath = os.path.join("C:/Users/Owner/git/python-challenge/PyPoll/Resources/election_data.csv")

#Set Variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

#Read CSV
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#Skip Header Row
    csv_header = next(csvreader)

    for row in csvreader:

#Determine Total Votes
        total_votes = total_votes + 1

#Determine Candidate Votes
        if row[2] == ("Charles Casper Stockham"):
            charles_votes += 1
        elif row[2] == ("Diana DeGette"):
            diana_votes += 1
        elif row[2] == ("Raymon Anthony Doane"):
            raymon_votes += 1

#Determine Candidate Percentage Votes
charles_percentage = round(((charles_votes / total_votes)*100), 3)
diana_percentage = round(((diana_votes / total_votes)*100), 3)
raymon_percentage = round(((raymon_votes / total_votes)*100), 3)

#Determine Winner
if charles_percentage > max(diana_percentage, raymon_percentage):
    winner = "Charles Casper Stockham"
elif diana_percentage > max(charles_percentage, raymon_percentage):
    winner = "Diana DeGette"
elif raymon_percentage > max(charles_percentage, diana_percentage):
    winner = "Raymon Anthony Doane"

#Print Results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
print(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#Set Text Path
textpath = os.path.join("C:/Users/Owner/git/python-challenge/PyPoll/analysis/output.txt")

#Write Text File
with open(textpath, 'w') as textfile:

    textfile.write("Election Results\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n")
    textfile.write(f"Diana DeGette: {diana_percentage}% ({diana_votes})\n")
    textfile.write(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------------\n")
     



