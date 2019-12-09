import os
import csv
votesList=[]
candidates=[]
candidatesCounts=[]

def loadData():
    csvpath = os.path.join( 'Resources', 'test_data.csv')
    with open(csvpath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
            #print(f"CSV Header: {csv_header}")
            for row in csvreader:
                    votesList.append(row)
                    #print(row)

def determineCandidates(listA):
    candidate_list=[]
    for x in listA:
            if x[2] not in candidate_list:
                candidate_list.append(x[2])
                #print(x[2])
   # for x in candidate_list:
   #     print(x)  
    return candidate_list               

def countVotes():
    counter=0
    for x in candidates:
        for y in votesList:
            if y[2]==x:
              counter=counter+1
        row=[x,counter]     
        print(f" {x}: {counter}")  
        candidatesCounts.append(row)
    counter=0          
              



loadData()
print(votesList)
candidates=determineCandidates(votesList)
print(candidates)
countVotes()
print(candidatesCounts)