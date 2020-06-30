import os
import csv
f=open('Analysis\PyBank_analysis.txt', 'w')
csvpath = os.path.join("Resources", "budget_data.csv")

count=[]
profitLoss=[]
change=[]
date=[]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(csv_header)

    count=0
    profitLoss = 0
    profitLoss_first = 0

    for row in csvreader:
        count += int(1)
        date = str(row[0])
        profitLoss += int(row[1])
    
        profitLoss_second = int(row[1])
        change_value = profitLoss_second - profitLoss_first 
        change.append(change_value)
        profitLoss_first = int(row[1])

    avgchange = (sum(change)-change[0])/int(count-1)
    format_avgchange=format(avgchange, ".2f")
    maxProfit = max(change)
    minProfit = min(change)

    #I couldnt get my date to correspond to the max/min change. I know its wrong.
    # Print report
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(count)}")
    print(f"Total: ${str(profitLoss)}")
    print(f"Average Change: ${format_avgchange}")
    print(f"Greatest Increase in Profits: {str(date)} (${int(maxProfit)})")
    print(f"Greastest Decrease in Profits: {str(date)} (${int(minProfit)})")

    f.write(f"Financial Analysis\n----------------------------\nTotal Months: {str(count)}\nTotal: ${str(profitLoss)}\nAverage Change: ${(format_avgchange)}\nGreatest Increase in Profits: {str(date)} (${int(maxProfit)})\nGreastest Decrease in Profits: {str(date)} (${int(minProfit)})")
f.close()