import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline='') as csv_file:
    bank_data = list(csv.reader(csv_file, delimiter=','))
total_profits = 0
total_months = 0
monthly_change = 0
max_increase = 0
max_decrease = 0


for i in range(1, len(bank_data)):
    for j in range(1, len(bank_data[i])):
        total_profits += int(bank_data[i][j])
        total_months += 1

# This loop increments the total of changes between months to find the total,
# since it is iterating over the same range necessary to find min/max, the
# if statements find and store the max increase/decrease with the corresponding month

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

analysis = os.path.join("results.txt")


with open(analysis, "w") as datafile:

    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${total_profits}\n")
    datafile.write(f"Average Change: ${round(average_change, 2)}\n")
    datafile.write(f"Greatest Increase in Profits: {max_month} (${max_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {min_month} (${max_decrease})\n")


print(f"Total: {total_months}")
print(f"Total Months: {total_profits}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")




