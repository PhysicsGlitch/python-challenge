# Disclaimer: I did this homework very early before we covered much of python.
# It was more intuitive for me to simply use csv.reader to compile a list
# and then I used for loops to references the indexes of the compiled list I needed.
# Instead of re-writing my code iterating with the csv.reader, I thought it was more efficient to direct the extra time
# to the challenges and demonstrate that I could use the csv.reader and csv.writer functionality in those assignments.
# It also was very helpful to do the task in different ways to conceptually understand the logic
# of how python works in different ways.

# Overview: The code has three main steps:
# Step 1: Use csv.reader to create a Python list of the data
# Step 2: Define my variables and then create for loops to increment the values I need to find.
# Step 3: Use csv.reader to convert my variables into a text file

# Step 1: Import os and csv and then use csv.reader to compile a bank_data list
import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline='') as csv_file:
    bank_data = list(csv.reader(csv_file, delimiter=','))

# Step 2: Define variables and create for loops to increment the totals.

total_profits = 0
total_months = 0
monthly_change = 0
max_increase = 0
max_decrease = 0

# Nested for loop to increment totals.

for i in range(1, len(bank_data)):
    for j in range(1, len(bank_data[i])):
        total_profits += int(bank_data[i][j])
        total_months += 1

# This next for loop increments the total of changes between months to find the total value for monthly_change,
# since it is iterating over the same range necessary to find min/max, the
# if statements find and store the max increase/decrease with the corresponding month. The range(1, len(bank_data)-1)
# ignores the header row and then the number of changes between months will always be one less than the total
# number of months.

for i in range(1, len(bank_data)-1):
    for j in range(1, len(bank_data[i])):
        monthly_change += int(bank_data[i+1][j])-int(bank_data[i][j])
        if int(bank_data[i+1][j])-int(bank_data[i][j]) > max_increase:
            max_increase = int(bank_data[i+1][j]) - int(bank_data[i][j])
            max_month = bank_data[i+1][0]
        if int(bank_data[i+1][j])-int(bank_data[i][j]) < max_decrease:
            max_decrease = int(bank_data[i+1][j]) - int(bank_data[i][j])
            min_month = bank_data[i+1][0]

average_change = monthly_change/(len(bank_data) -2)
# the -2 from len is to eliminate the header
# and the number of changes between months will always be one less than total months so - 2 from len gives the
# correct value of monthly changes to divide the total change by to get the average.

# Format months: I used the split method and a formatted string to make the month readout look identical
# to how it appeared in the readme file.

split_min_month = min_month.split('-')
split_max_month = max_month.split('-')

formatted_min_month = f"{split_min_month[1]}-20{split_min_month[0]}"
formatted_max_month = f"{split_max_month[1]}-20{split_max_month[0]}"


# Creates a path to the results text file.
analysis = os.path.join("results.txt")

# I used formatted strings and \n to create new lines to print a basic text file.

with open(analysis, "w") as datafile:

    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${total_profits}\n")
    datafile.write(f"Average Change: ${round(average_change, 2)}\n")
    datafile.write(f"Greatest Increase in Profits: {formatted_max_month} (${max_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {formatted_min_month} (${max_decrease})\n")


print(f"Total: {total_months}")
print(f"Total Months: {total_profits}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {formatted_max_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {formatted_min_month} (${max_decrease})")




