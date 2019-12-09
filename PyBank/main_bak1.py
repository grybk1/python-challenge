# pybank challange - Gilbert Rybak 

import os
import csv

#init data structures
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
        #print(csvreader)
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")
        
        for row in csvreader:
            #Calc totalMonthsS
            row.append('0') #init changeValue column
            totalMonths=totalMonths+1
            budgetList.append(row)
#            budgetDict['ID']=totalMonths
#            budgetDict['Date']=row[0]
#            budgetDict['P&L']=row[1]
#            budgetDict['Change']=0
            
            #Calc totalProfits
            if int(row[1]) >=0:
              totalProfits=totalProfits+int(row[1])
            #Calc totalLosses
            if int(row[1]) <=0:
              totalLosses=totalLosses+int(row[1])
#            print(row)
#            print(row[1])
            #print(totalMonths)
#        print(f'Toal Months: {totalMonths}')
#        print (f"Total Profits: "+str(totalProfits))
#        print (f"TotalLosses: {totalLosses}")


# loop to calc change over month
print("Begin budgetlist loop")
for x in range(1,len(budgetList)):
   #print(x)
#   budgetList[x][2]=int(x)
#   print(f'current value: {int(budgetList[x][1])}')
#   print(f'previous value: {int(budgetList[x-1][1])}') 
  # if int(budgetList[x-1][1]) >=0: 
    budgetList[x][2]=int(budgetList[x][1])-int(budgetList[x-1][1])
  # else: 
  #  budgetList[x][2]=int(budgetList[x][1])+int(budgetList[x-1][1])
    print(budgetList[x])
#print(budgetList)
print("end budget list loop")

#change number is off
def calcAverageChange():
    totalChange=0
    for x in range(len(budgetList)):
        totalChange=totalChange+int(budgetList[x][2])
    aveChange=totalChange/(int(len(budgetList))-1)    
#    print(totalChange)
#    print(len(budgetList))
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
#print("Change Calculation")
#print(budgetList[0])
#print(budgetList[1])
#print(budgetList[2])
#budgetList[2][2]=int(budgetList[1][1])-int(budgetList[0][1])
#print(budgetList[2][2])
#print ("Length of budget list:")
#print(len(budgetList))






print(f'Toal Months: {totalMonths}')
#print (f"Total Profits: "+str(totalProfits))
#print (f"TotalLosses: {totalLosses}") 
print (f"Net Total: ${totalProfits+totalLosses}" )
print (f"Average Change:  ${calcAverageChange()}")
print (f"Greatest Increase in Profits ${calcGreatestIncrease()}")
print (f"Greatest Decrease in Profits ${calcGreatestDecrease()}")
#print(budgetList)
#print("indexed below:")
#print(budgetList[3])
#print(budgetList[3][2])


