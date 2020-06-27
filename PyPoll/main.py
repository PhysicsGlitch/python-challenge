import os
import csv

election_data_original = os.path.join('Resources', 'election_data.csv')

with open(election_data_original, newline='') as csv_file:
    election_data = list(csv.reader(csv_file, delimiter=','))

# The next section is my code for finding all the unique candidates.
# I know it is expensive to iterate over the massive list twice. I could have put the two four loops together to iterate
# only once. But from a space perspective, looping through once to find all the unique candidates and then looping
# again to # tally vote count was more concise. I commented out the loop I ran to find the unique candidates below,
# but I ran it and then created variables for the names of the candidates.

# unique_candidates = []
# for row in range(1, len(election_data)):
  #  for name in range(2, len(election_data[row])):
   #     if election_data[row][name] not in unique_candidates:
    #        unique_candidates.append(election_data[row][name])

 # print(unique_candidates)


# To tally vote count I iterated through the list and then had four if statements that incremented vote tally
# by 1 if the candidate name matched in index 2 of the row. I also created a total_votes count that incremented
# each vote cast.

total_votes = 0
kahn_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

for i in range(1, len(election_data)):
    for j in range(2, len(election_data[i])):
        total_votes += 1
        if election_data[i][2] == "Khan":
            kahn_total += 1
        elif election_data[i][2] == "Correy":
            correy_total += 1
        elif election_data[i][2] == "Li":
            li_total += 1
        elif election_data[i][2] == "O'Tooley":
            otooley_total += 1

# To find the winner and the rankings I created a list that records the name, percent and total vote count
# into a row. Then I used itemgetter from the operator package to sort the list by index[2] or total vote
# count which let me easily print out the winner and rankings by referencing the right index in my list.

candidate_list = []
candidate_list.append(["Kahn", "{:.3%}".format(kahn_total/total_votes), kahn_total])
candidate_list.append(["Correy", "{:.3%}".format(correy_total/total_votes), correy_total])
candidate_list.append(["Li", "{:.3%}".format(li_total/total_votes), li_total])
candidate_list.append(["O'Tooley", "{:.3%}".format(otooley_total/total_votes), otooley_total])

from operator import itemgetter
sorted_candidates = sorted(candidate_list, key=itemgetter(2))

# This texts creates a path to my text file and then prints out the results on the terminal and writes them to text.

analysis = os.path.join("election_results.txt")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{sorted_candidates[-1][0]}: {sorted_candidates[-1][1]} ({sorted_candidates[-1][2]})")
print(f"{sorted_candidates[2][0]}: {sorted_candidates[2][1]} ({sorted_candidates[2][2]})")
print(f"{sorted_candidates[1][0]}: {sorted_candidates[1][1]} ({sorted_candidates[1][2]})")
print(f"{sorted_candidates[0][0]}: {sorted_candidates[0][1]} ({sorted_candidates[0][2]})")
print("-------------------------")
print(f"Winner: {sorted_candidates[-1][0]}")
print("-------------------------")

with open(analysis, "w") as datafile:

    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("-------------------------\n")
    datafile.write(f"{sorted_candidates[-1][0]}: {sorted_candidates[-1][1]} ({sorted_candidates[-1][2]})\n")
    datafile.write(f"{sorted_candidates[2][0]}: {sorted_candidates[2][1]} ({sorted_candidates[2][2]})\n")
    datafile.write(f"{sorted_candidates[1][0]}: {sorted_candidates[1][1]} ({sorted_candidates[1][2]})\n")
    datafile.write(f"{sorted_candidates[0][0]}: {sorted_candidates[0][1]} ({sorted_candidates[0][2]})\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {sorted_candidates[-1][0]}\n")
    datafile.write("-------------------------\n")