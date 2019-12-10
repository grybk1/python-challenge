import os
import csv
votesList=[]
candidates=[]
candidatesCounts=[]

def loadData():
    #csvpath = os.path.join( 'Resources', 'test_data.csv')
    csvpath = os.path.join( 'Resources', 'election_data.csv')
    with open(csvpath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
            #print(f"CSV Header: {csv_header}")
            for row in csvreader:
                    votesList.append(row)
                    

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
        #print(f" {x}: {counter}")  
        candidatesCounts.append(row)
    counter=0          

def countVotes2():
    votesList[1].count('Correy')

countVotes2()

def printResults():
    #calc total votes
#    totalVotes=0
#    candidateTotalCounts=0
#    for x in candidatesCounts:
#       totalVotes=totalVotes+x[1]
#        print(f"{x[0]}: {x[1]}")
    totalVotes=votesList.__len__()
    print("Election Results")
    print("----------------------")

    print(f"Total Votes: {totalVotes}") 
    print("----------------------")   
    winner=''
    topVotes=0
    for x in candidatesCounts:
        winPercentage=(x[1]/totalVotes)*100
        print(f"{x[0]}: {winPercentage.__round__(3)}%  {x[1]}")
        if x[1]>topVotes:
            topVotes=x[1]
            winner=x[0]
    print("----------------------")
    print("Winner :" +winner) 
    print("----------------------")
    #write results to file
    outputFile=open("Output/results.txt","w" )
    outputFile.write("Election Results\n")
    outputFile.write("----------------------\n")
    outputFile.write(f"Total Votes: {totalVotes}\n") 
    outputFile.write("----------------------\n")  
    winner=''
    topVotes=0
    for x in candidatesCounts:
        winPercentage=(x[1]/totalVotes)*100
        outputFile.write(f"{x[0]}: {winPercentage.__round__(3)}%  {x[1]}\n")
        if x[1]>topVotes:
            topVotes=x[1]
            winner=x[0]
    outputFile.write("----------------------\n")
    outputFile.write("Winner :" +winner+"\n") 
    outputFile.write("----------------------\n")
     
 


loadData()
#print(votesList)
candidates=determineCandidates(votesList)
#print(candidates)
countVotes()
#print(candidatesCounts)
printResults()