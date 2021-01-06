# python Main.py > Analysis/Results.txt
import os
import csv
import collections

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
open_csv = open(csvpath)

vote = collections.Counter()
# Making sure Python reads the code correctly
with open_csv as f:
    pollreader = csv.reader(f, delimiter = ",")
    header = next(pollreader)

# Counting the number of votes for everyone  
    for row in pollreader:
        vote[row[2]] += 1
#print('Number of Khan votes: %s' %vote['Khan'])
print(vote.most_common())

    # Counting the # of dates in the the dataset
#total = len(list(pollreader))
#print(total)

    #ctr = 0
    # Counting the number of votes for Khan
    #for khan_counter in pollreader:
       # if khan_counter[2] == 'Khan':
        #    ctr += 1
   # print(ctr)

