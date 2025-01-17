# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path - does not work because of spaces in path name
file_to_load = r"C:\Users\asg_a_1p8y6mm\OneDrive\Desktop\WIOA Training\DataAnalytics\Module 3\Module 3; Class Challenge\python-challenge\PyPoll\Resources\election_data.csv"
#file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file  - does not work because of spaces in path name
file_to_output = r"C:\Users\asg_a_1p8y6mm\OneDrive\Desktop\WIOA Training\DataAnalytics\Module 3\Module 3; Class Challenge\python-challenge\PyPoll\analysis\election_analysis.txt"

# Initialize variables to track the election data
total_votes = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Assuming 'Candidate' is the third column

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Determine the winner
for candidate, count in candidate_votes.items():
    if count > winning_count:
        winning_count = count
        winning_candidate = candidate

# Open a text file to save the  - as specified in the assignment
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n\n")
    txt_file.write("-------------------------\n\n")
    txt_file.write(f"Total Votes: {total_votes}\n\n")
    txt_file.write("-------------------------\n\n")

    for candidate, count in candidate_votes.items():
        percentage = (count / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({count})\n\n")

    txt_file.write("-------------------------\n\n")
    txt_file.write(f"Winner: {winning_candidate}\n\n")
    txt_file.write("-------------------------")

# Print the results to the terminal
print("Election Results\n\n")
print("-------------------------\n\n")
print(f"Total Votes: {total_votes}\n\n")
print("-------------------------\n\n")

for candidate, count in candidate_votes.items():
    percentage = (count / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({count})\n\n")

print("-------------------------\n\n")
print(f"Winner: {winning_candidate}\n\n")
print("-------------------------")

# Print the results to the terminal - as specified in the assignment
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")

for candidate, count in candidate_votes.items():
    percentage = (count / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({count})\n")

print("-------------------------\n")
print(f"Winner: {winning_candidate}\n")
print("-------------------------\n")

# Open a text file to save the output - modified approach for greater clarity
#with open(file_to_output, "w") as txt_file:
#    txt_file.write("Election Results\n-------------------------\n")
#    txt_file.write(f"Total Votes: {total_votes}\n")
#    txt_file.write("-------------------------\n")

#    for candidate, count in candidate_votes.items():
#        percentage = (count / total_votes) * 100
#        txt_file.write(f"{candidate}: {percentage:.2f}% ({count})\n")

#    txt_file.write("-------------------------\n")
#    txt_file.write(f"Winner: {winning_candidate}\n")
#    txt_file.write("-------------------------")

# Print the results to the terminal - modified approach for greater clarity
#print("Election Results")
#print("-------------------------")
#print(f"Total Votes: {total_votes}")
#print("-------------------------")

#for candidate, count in candidate_votes.items():
#    percentage = (count / total_votes) * 100
#    print(f"{candidate}: {percentage:.2f}% ({count})")

#print("-------------------------")
#print(f"Winner: {winning_candidate}")
#print("-------------------------")