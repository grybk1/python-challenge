# pybank challange - Gilbert Rybak 
import csv
import os
 
#init variables
totalMonths=0
totalProfits=0
totalLosses=0
totalChange=0
lastMonthPL=0
budgetList=[]

#load data
csvpath = os.path.join( 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
            #print(f"CSV Header: {csv_header}")
            for row in csvreader:
            #Calc totalMonths
               totalMonths=totalMonths+1
            #Populate budgetList
               row.append('0') #init changeValue column 
               budgetList.append(row)
            #Calc totalProfits
               if int(row[1]) >=0:
                totalProfits=totalProfits+int(row[1])
            #Calc totalLosses
               if int(row[1]) <=0:
                 totalLosses=totalLosses+int(row[1])


def calcChangeOverMonth():
# loop to calc change over month
    for x in range(1,len(budgetList)):
      budgetList[x][2]=int(budgetList[x][1])-int(budgetList[x-1][1])

def calcAverageChange():
    totalChange=0
    for x in range(len(budgetList)):
        totalChange=totalChange+int(budgetList[x][2])
    aveChange=totalChange/(int(len(budgetList))-1)    
    return aveChange.__round__(2)

def calcGreatestIncrease():
        greatestIncreaseMonth=''
        greatestIncreaseAmount=0
        for x in range(len(budgetList)):
            if int(budgetList[x][2])>greatestIncreaseAmount:
                greatestIncreaseAmount=int(budgetList[x][2])
                greatestIncreaseMonth=budgetList[x][0]
        return str(greatestIncreaseMonth)+' '+str(greatestIncreaseAmount)            

def calcGreatestDecrease():
        greatestDecreaseMonth=''
        greatestDecreaseAmount=0
        for x in range(len(budgetList)):
            if int(budgetList[x][2])<greatestDecreaseAmount:
                greatestDecreaseAmount=int(budgetList[x][2])
                greatestDecreaseMonth=budgetList[x][0]
        return str(greatestDecreaseMonth)+' '+str(greatestDecreaseAmount) 


#write data files
def writeResultsData():
    output_path = os.path.join("Output", "OutputData.csv")
    with open(output_path, 'w', newline='') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        # Write the first row (column headers)
        csvwriter.writerow(['Date', 'ProfitLoss', 'MonthPLChange'])
        # Write all rows
        for x in range(len(budgetList)):
            csvwriter.writerow(budgetList[x])

#write results file
def writeResultsFile():
    outputFile=open("Output/results.txt","w" )
    outputFile.write(f'Toal Months: {totalMonths}\n')
    outputFile.write(f"Net Total: ${totalProfits+totalLosses}\n" )
    outputFile.write(f"Average Change:  ${calcAverageChange()}\n")
    outputFile.write(f"Greatest Increase in Profits ${calcGreatestIncrease()}\n")
    outputFile.write(f"Greatest Decrease in Profits ${calcGreatestDecrease()}\n")

#Print Results to Console
def printResultsToConsle():
    print(f'Toal Months: {totalMonths}')
    print (f"Net Total: ${totalProfits+totalLosses}" )
    print (f"Average Change:  ${calcAverageChange()}")
    print (f"Greatest Increase in Profits ${calcGreatestIncrease()}")
    print (f"Greatest Decrease in Profits ${calcGreatestDecrease()}")



calcChangeOverMonth()
writeResultsData()
writeResultsFile()
printResultsToConsle()
