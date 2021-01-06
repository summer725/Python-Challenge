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

    # Counting the # of dates in the the dataset
    #total = len(list(bankreader))
    #print(total)

    # Find the net profits/losses for the entire set
    sums = 0
    count = 0
    for row in bankreader:
        sums = sums + float(row[1])
        count += 1
    print("Total Months: ", count)
    print("Total: ", '$%s' %(sums))