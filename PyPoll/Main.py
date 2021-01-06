# python Main.py > Analysis/Results.txt
import os
import csv
import collections

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
open_csv = open(csvpath)

print("Election Results")
print("---------------------------")
vote = collections.Counter()
# Making sure Python reads the code correctly
with open_csv as f:
    pollreader = csv.reader(f, delimiter = ",")
    header = next(pollreader)

# Counting the number of votes for everyone
    dates = 0
    for row in pollreader:
        vote[row[2]] += 1
        dates += 1

#print(vote.most_common())

print("Total Votes: ", dates)
print("---------------------------")
## Khan Votes
#k = ('Khan: (%s)' %vote['Khan'])
khan = vote['Khan']
calculation_k = (khan/3521001)*100
khan_percent = round(calculation_k, 3)
print("Khan: ", khan_percent, "%", "(%s)"%(khan))

## Correy Votes
correy = vote['Correy']
calculation_c = (correy/3521001)*100
correy_percent = round(calculation_c, 3)
print("Correy: ", correy_percent, "%", "(%s)"%(correy))   

## Li Votes
li = vote['Li']
calculation_l = (li/3521001)*100
li_percent = round(calculation_l, 3)
print("Li: ", li_percent, "%", "(%s)"%(li))

## O'Tooley Votes
o = vote["O'Tooley"]
calculation_o = (o/3521001)*100
o_percent = round(calculation_o, 3)
print("O'Tooley: ", o_percent, "%", "(%s)"%(o))

print("---------------------------")
print("Winner: Khan")
print("---------------------------")