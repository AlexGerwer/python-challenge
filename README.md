PYTHON-CHALLENGE

PyBank main.py
Explanation:
1.	Import Libraries:
o	csv: For reading and processing the CSV file.
o	os: For handling file paths.
2.	File Paths:
o	Set file_to_load to the path of your CSV file.
o	Set file_to_output to the desired path for the output text file.
3.	Variables:
o	total_months: Stores the total number of months.
o	total_net: Stores the total profit/loss over all months.
o	net_change_list: A list to store the changes in profit/loss between consecutive months.
o	greatest_increase_amount: Stores the maximum profit increase amount.
o	greatest_increase_month: Stores the month of the maximum profit increase.
o	greatest_decrease_amount: Stores the maximum profit decrease amount.
o	greatest_decrease_month: Stores the month of the maximum profit decrease.
4.	Open and Read CSV:
o	Open the CSV file using with open(file_to_load) as financial_data:.
o	Create a csv.reader object to read the data row by row.
o	Skip the header row using header = next(reader).
5.	Process Data:
o	Iterate through each row in the CSV using for row in reader:.
o	Increment total_months.
o	Add the current month's profit/loss to total_net.
o	Calculate the net change between the current month and the previous month (if it's not the first month).
o	Append the net change to net_change_list.
o	Update greatest_increase_amount and greatest_increase_month if the current net change is greater.
o	Update greatest_decrease_amount and greatest_decrease_month if the current net change is less.
6.	Calculate Average Change:
o	Calculate the average net change using sum(net_change_list) / len(net_change_list).
7.	Generate Output:
o	Create a formatted string output containing all the calculated values.
8.	Print and Write to File:
o	Print the output to the terminal using print(output).
o	Open the output text file (file_to_output) in write mode ("w") and write the output to it.

PyPoll main.py
Explanation:
1.	Import Modules: Import csv for reading the CSV file and os for file path handling.
2.	File Paths: Set the input and output file paths.
3.	Initialize Variables:
o	total_votes: Stores the total number of votes.
o	candidate_votes: A dictionary to store candidate names as keys and their vote counts as values.
o	winning_candidate: Stores the name of the winning candidate.
o	winning_count: Stores the number of votes the winner received.
4.	Open and Read CSV:
o	Open the CSV file using with open(file_to_load) as election_data:.
o	Create a csv.reader object to read the data row by row.
o	Skip the header row using header = next(reader).
5.	Process Data:
o	Loop through each row in the CSV using for row in reader:.
o	Increment total_votes for each row.
o	Extract the candidate's name from the third column (row[2]).
o	Update the candidate_votes dictionary:
	If the candidate is already in the dictionary, increment their vote count.
	If the candidate is new, add them to the dictionary with a vote count of 1.
6.	Determine the Winner:
o	Loop through the candidate_votes dictionary.
o	For each candidate, compare their vote count to winning_count.
o	If a candidate has more votes than the current winning_count, update winning_candidate and winning_count.
7.	Write Output to File:
o	Open the output text file using with open(file_to_output, "w") as txt_file:.
o	Write the election results to the file, including:
	Total votes
	Each candidate's name, vote count, and percentage
	The winner
8.	Print Output to Terminal:
o	Print the election results to the terminal using print() statements.
