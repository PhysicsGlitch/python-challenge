import os
import csv

employee_data = os.path.join('Resources', 'employee_data.csv')

with open(employee_data) as csv_file:
    employee_reader = csv.reader(employee_data)
    header =