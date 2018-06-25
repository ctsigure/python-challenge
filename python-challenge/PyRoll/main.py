import os
import csv

pyrollcsv = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")


with open(pyrollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    month = -1
    amount = []
    date = []
    for row in csvreader:
        month += 1
        date.append(row[0])
        amount.append(row[1])
        
        
    amount.pop(0)
    amount = list(map(int,amount))
    total_amount = sum(amount)
    average = total_amount / len(amount)
    greatest_increase = max(amount)
    greatest_decrease = min(amount)
    index_increase = amount.index(greatest_increase)
    index_decrease = amount.index(greatest_decrease)
    date_increase = date[index_increase + 1]
    date_decrease = date[index_decrease + 1]

    
    print("Financial Analysis: "+'\n'+'-' * 25+'\n'+
    "Total Months: " + str(month)+'\n'+
    "Total Net Amount: $" + str(total_amount)+'\n'+
    "Average: $" + str(average)+'\n'+
    "Greatest Increase in Profits: " + date_increase + " ($"+str(greatest_increase)+")"+'\n'+
    "Greatest Decrease in Profits: " + date_decrease + " ($"+str(greatest_decrease)+")")




   

