import os
import csv
import functools

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

    date.pop(0)
    new_date = []
    months = []
    years = []
    for d in date:
        new_date.append(d.split('-'))
    
    for k in new_date:
        months.append(k[0])
        years.append(k[1])   


    each_month = []
    value_each_month = 0
    i = 0
    while i < len(amount) - 1:
        value_each_month = amount[i + 1] - amount[i]
        each_month.append(value_each_month)
        i += 1
    

    total_each_month = sum(each_month)
    print(total_each_month)
    average = total_each_month / month
    greatest_increase = max(each_month)
    greatest_decrease = min(each_month)
    index_increase = each_month.index(greatest_increase)
    index_decrease = each_month.index(greatest_decrease)
    date_increase = months[index_increase + 1] + "-" + years[index_increase + 1]
    date_decrease = months[index_decrease + 1] + "-" + years[index_decrease + 1]

    
    my_result = "Financial Analysis: " + '\n' + '-' * 25 + '\n' + \
                "Total Months: " + str(month) + '\n' +\
                "Total Net Amount: $" + str(total_amount) + '\n' +\
                "Average: $" + str(average) + '\n' +\
                "Greatest Increase in Profits: " + date_increase + " ($"+str(greatest_increase)+")" + '\n' +\
                "Greatest Decrease in Profits: " + date_decrease + " ($"+str(greatest_decrease)+")"
   
    #print(my_result)


with open(os.path.join(os.path.dirname(__file__),"Financial Analysis.txt"), "w") as file:
    file.write(my_result)




   

