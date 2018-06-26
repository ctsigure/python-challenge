import os
import csv
import us_state


pybosscsv = os.path.join(os.path.dirname(__file__),"employee_data.csv")

with open(pybosscsv, "r") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

    with open("myfile.csv", "w", newline='') as newcvsfile:
        csvwriter = csv.writer(newcvsfile)
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        
        for row in csvreader:
            name = row[1].split()
            row[1] = name[0]
            row.insert(2, name[1])
            dob = row[3].split("-")
            row[3] = '/'.join([dob[1], dob[2], dob[0]])
            row[4] = '***-**-' + row[4][-4:]
            row[5] = us_state.us_state_abbrev[row[5]]

            csvwriter.writerow(row)
            
     





    
