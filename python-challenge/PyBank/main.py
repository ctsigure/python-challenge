import os
import csv

pybankcsv = os.path.join(os.path.dirname(__file__),"Resources","election_data.csv")

with open(pybankcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    vote = -1
    can_list = []
    for row in csvreader:
        vote += 1
        can_list.append(row[2])
    can_list.pop(0)

    khan = 0
    correy = 0
    li = 0
    otooley = 0
    for i in can_list:
        if i == "Khan":
            khan += 1
        elif i == "Correy":
            correy += 1
        elif i == "Li":
            li += 1
        else:
            otooley += 1

    percent_khan = round(khan/vote * 100, 2)
    percent_correy = round(correy/vote * 100,2)
    percent_li = round(li/vote * 100,2)
    percent_otooley = round(otooley/vote * 100,2)

    winner_cals = max(khan,correy,li,otooley)
    cans = ["Khan","Correy","Li","O'Tooley"]
    total_per_can = [khan, correy, li, otooley]
    new_list = list(zip(cans,total_per_can))
   
    winner = 0
    for j in new_list:
        if winner_cals == j[1]:
            winner = j[0]
            



    my_result = "Election Results" + '\n' + '-' * 25 + '\n' +\
    "Total Votes: " + str(vote) + '\n' + '-' * 25 + '\n' +\
    "Khan: " + str(percent_khan) +'% (' + str(khan) + ')' + '\n'+\
    "Correy: " + str(percent_correy) + '% (' + str(correy) + ')' + '\n' +\
    "Li: " + str(percent_li) + '% (' + str(li) + ')' + '\n' +\
    "O'Tooley: " + str(percent_otooley) + '% ('+str(otooley) + ')' + '\n' + '-' * 25 + '\n' +\
    "Winner: " + winner
    print(my_result)

    with open(os.path.join(os.path.dirname(__file__),"Election Results.txt"), "w") as file:
        file.write(my_result)

