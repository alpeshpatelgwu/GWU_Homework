import os
import csv
import pandas as pd 

#electionpath = os.path.join('..', 'resources', 'election_data.csv')

print("This is HW Assignment #3")
print("")

# Create a variable that holds the import of the Budget_Data CSV File
# budgetpath = os.path.join('..', 'resources', 'budget_data.csv')
budgetpath = "C:\\Users\\aipat\\python-challenge\\resources\\budget_data.csv"

months = []
total = []
profitloss = []

with open(budgetpath, 'r') as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=",")
    budgetheader = next(budgetreader)
    
  
    #this will iterate through each row of the csv file and read it
    #this for loop will continue to loop through the csvfile till 
    #it reaches the end
    # === What do you want to do in this loop? ===
    for row in budgetreader:
        #print(f'{row[0]} {row[1]}')
        #print(f'{row[1]}')
        
        #this will store the values of each column in either months list or total list
        months.append(row[0])
        total.append(int(row[1]))
        
    # iterate through to calculate the profit/loss change
    for i in range(len(total)-1):
        profitloss.append(total[i+1]-total[i])       
          
totalsum = sum(int(x) for x in total)

avgchange = round(sum(profitloss)/len(profitloss),2)

#Calculate the max/min profit loss
increase_profit = max(profitloss)
decrease_loss = min(profitloss)

#Calculate the max months to try to associate with profit/loss
increase_months = months[profitloss.index(increase_profit) + 1]
decrease_months = months[profitloss.index(decrease_loss) + 1]

print("============================================================")
print("")
print(f'There are a total of {len(months)} months')
print("")
print(f'The total profit/loss margin is ${totalsum}')
print(f'The average change is ${avgchange}')
print(f'The Max Increase value is {(increase_months)} ${increase_profit}')
print(f'The Max Decrease value is {(decrease_months)} ${decrease_loss}')
print("")
print("This is the end of Bank Analysis")
print("============================================================")

output_analysis = "C:\\Users\\aipat\\python-challenge\\PyBank\\PyBankAnalysis.txt"

with open(output_analysis, 'w') as analysisfile:

	analysisfile.write("============================================================")
	analysisfile.write("\n")
	analysisfile.write("This is your financial analysis of Py Bank")
	analysisfile.write("\n")
	analysisfile.write(f'There are a total of {len(months)} months')
	analysisfile.write("\n")	
	analysisfile.write(f'The total profit/loss margin is ${totalsum}')
	analysisfile.write("\n")	
	analysisfile.write(f'The average change is ${avgchange}')
	analysisfile.write("\n")	
	analysisfile.write(f'The Max Increase value is {(increase_months)} ${increase_profit}')
	analysisfile.write("\n")	
	analysisfile.write(f'The Max Decrease value is {(decrease_months)} ${decrease_loss}')
	analysisfile.write("\n")	
	analysisfile.write("This is the end of Bank Analysis")
	analysisfile.write("\n")	
	analysisfile.write("============================================================")
	