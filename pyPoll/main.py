# PyPoll Solution Gilbert Rybak
import os
import csv

#variable collections
votesList=[]        #holds imported CSV
candidates=[]       #holds list of candidates 
candidatesCounts=[] #holds election results


#Import CSV file
def loadData():
    #csvpath = os.path.join( 'Resources', 'test_data.csv')
    csvpath = os.path.join( 'Resources', 'election_data.csv')
    with open(csvpath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            #skip header
            csv_header = next(csvreader)
            #print(f"CSV Header: {csv_header}")
            for row in csvreader:
                    votesList.append(row)
                    #print(row)


#Get list of candidates from full dataset    
def determineCandidates(listA):
    candidate_list=[]
    for x in listA:
            if x[2] not in candidate_list:
                candidate_list.append(x[2])
    return candidate_list               

#Collect election results
def countVotes():
    votes=[]
    for y in votesList:
       votes.append(y[2])
       #print(votes)
    for x in candidates:
        row=[x,votes.count(x)]
        candidatesCounts.append(row)           
        #print(row)
    #print(candidatesCounts)

   
#Save to text file
def saveResults():
    #print(candidatesCounts)
    totalCount=votesList.__len__()
    winner=''
    topVotes=0
    outputFile=open("Output/results.txt","w" )
    outputFile.write("Election Results\n")
    outputFile.write("----------------------\n")
    outputFile.write(f"Total Votes: {totalCount}\n") 
    outputFile.write("----------------------\n")          
    for x in candidatesCounts:
        winPercentage=(x[1]/totalCount)*100
        outputFile.write(f"{x[0]}: {winPercentage.__round__(3)}%  {x[1]}\n")
        if x[1]>topVotes:
            topVotes=x[1]
            winner=x[0]
    outputFile.write("----------------------\n")
    outputFile.write("Winner :" +winner+"\n") 
    outputFile.write("----------------------\n")
    outputFile.close()    

#Retrieve from text file for display     
def displayResults():
    inputFile=open("Output/results.txt")  
    for row in inputFile:
        print(row)
    

#MAIN SECTION     
loadData()
candidates=determineCandidates(votesList)
countVotes()
saveResults()
displayResults()




