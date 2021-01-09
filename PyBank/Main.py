#python Main.py > Analysis/Results.txt
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
open_csv = open(csvpath)

print("Financial Analysis")
print("------------------------")
# Making sure Python reads the code correctly
with open_csv as f:
    bankreader = csv.reader(f, delimiter = ",")
    header = next(bankreader)
    
    # Find the net profits/losses for the entire set
    sums = 0
    count = 0
    previous = 0
    diff = [] #setting up to be a list
    months = [] #setting up to be a list
    for row in bankreader:
        diff = diff + [(float(row[1])- previous)]
        months = months + [row[0]]
        sums = sums + float(row[1])
        count += 1
        #print(float(row[1])-previous)
        previous = float(row[1])
        
    print("Total Months: ", count)
    print("Total: ", '$%s' %(round(sums)))
    x = sum(diff[1:])/(count-1)
    print(f"Average Change: ${x:.2f}")
    #print(diff)
    #Max Change
    #print(diff.index(max(diff)))
    #print(months)
    print("Greatest Increase in Profits: ", months[diff.index(max(diff))], '($%s)' %(round(max(diff)))) # max month name 
    #print(max(diff)) # max value

    #Min Change
    #print(diff.index(min(diff)))
    #print(months)
    print("Greatest Decrease in Profits: ", months[diff.index(min(diff))], '($%s)' %(round(min(diff)))) # min month name
    #print(min(diff)) #min value
