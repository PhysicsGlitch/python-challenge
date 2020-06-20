import os
import csv

employee_data = os.path.join('Resources', 'employee_data.csv')
formatted_employee_data = os.path.join('Resources', 'formatted_employee_data.csv')

# There may be a more elegant way to do this, but a simple way was to design my code in 3 Steps:
# Step 1: Separate the CSV into individual lists using csv.reader
# Step 2: Reformat the lists into correct formats
# Step 3: Recombine the reformatted lists with csv.writer

#Define necessary lists to append data
employee_id = []
names = []
birth_date = []
birth_split = []
ssn = []
state = []

with open(employee_data, 'r') as old_data:
    employee_reader = csv.reader(old_data, delimiter=',')
    next(employee_reader)
    for row in employee_reader:
        employee_id.append(row[0])
        names.append(row[1].split())
        birth_date.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

#The first and last name were split above so the name file alread has a list with first and last.
# A list comprehension creates individual list of first and last names.

first_name = [name[0] for name in names]
last_name = [name[1] for name in names]

# This loop creates a formatted string which adds the final 4 digits of ssn. N.B. I know it is better
# practice to use the join method than a formatted string. But I am just trying to get functions that work
# and then integrate best practices as I become more proficient.

formatted_ssn = []
for ss_id in ssn:
    formatted_ssn.append(f"***_**_{ss_id[7:]}")

# Split birth into three element based on the - delimiter and then recombine with a formatted string as with ssn.
for birth in birth_date:
    birth_split.append(birth.split("-"))

birth_formatted = [f"{birth[1]}/{birth[2]}/{birth[0]}" for birth in birth_split]

# This is the dictionary for state abbreviation conversion. Again, I know I should put this in a separate file in
# resources and then reference there, but taking it one step at a time.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# This creates a list comprehension that substitutes the full state name for the abbreviation based on referencing the dictionary.

state_formatted = [us_state_abbrev[state_name] for state_name in state]

# This is the new header for the formatted file.

header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]

# This code uses csv.writer to recombine my lists into the appropriate rows. I found the most intuitive way was to
# construct a for loop that writes each row as a list. But I think there is a way to use writerows with an iterable as well.
# I just used the range of employee-id as the index range for my for loop and then referenced every list base on that
# index to write the correct row.

with open(formatted_employee_data, 'w', newline='') as formatted_data:
    employee_writer = csv.writer(formatted_data, dialect='excel')
    employee_writer.writerow(header)
    for item in range(len(employee_id)):
        employee_writer.writerow([employee_id[item],
                                  first_name[item],
                                  last_name[item],
                                  birth_formatted[item],
                                  formatted_ssn[item],
                                  state_formatted[item]])

# The final Excel document is exported as a Excel dialect CSV. I opened the formatted_employee_data.csv in excel
# and it displayed correctly.





