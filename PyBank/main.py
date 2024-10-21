# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path - does not work because of spaces in path name
file_to_load = r"C:\Users\asg_a_1p8y6mm\OneDrive\Desktop\WIOA Training\DataAnalytics\Module 3\Module 3; Class Challenge\python-challenge\PyBank\Resources\budget_data.csv"
#file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path - does not work because of spaces in path name
file_to_output =r"C:\Users\asg_a_1p8y6mm\OneDrive\Desktop\WIOA Training\DataAnalytics\Module 3\Module 3; Class Challenge\python-challenge\PyBank\analysis\budget_analysis.txt"

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
greatest_increase_amount = 0
greatest_increase_month = ""
greatest_decrease_amount = 0
greatest_decrease_month = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])

        # Calculate net change
        if total_months > 1:
            net_change = int(row[1]) - previous_profit
            net_change_list.append(net_change)

            # Update greatest increase
            if net_change > greatest_increase_amount:
                greatest_increase_amount = net_change
                greatest_increase_month = row[0]

            # Update greatest decrease
            if net_change < greatest_decrease_amount:
                greatest_decrease_amount = net_change
                greatest_decrease_month = row[0]

        previous_profit = int(row[1])

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary according to assignment specifications
output = f"Financial Analysis\n\n----------------------------\n\nTotal Months: {total_months}\n\nTotal: ${total_net}\n\nAverage Change: ${average_change:.2f}\n\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\n\n"

# Generate the output summary according to an arguably clearer format
#output = f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${total_net:,}\nAverage Change: ${average_change:,.2f}\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount:,})\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount:,})\n"

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
