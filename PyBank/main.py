'''
    Open and read csv
    Skip header
    Find the total number of months 
    Find the avg of changes in profit/loss
    find the greatest increase in profit, date and month
    Find the greatest decrease in losses, date and month
'''

import os
import csv

#Find path
budget_data = os.path("Resources", "budget_data")

#Open and Read
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Read header row first
    csv_header=next(csvfile)

    print(len(row(0))