import os
import csv

cwd = os.getcwd()
bankdat_path = os.path.join(cwd, "PyBank", "Resources", "budget_data.csv")

with open(bankdat_path, 'r') as bankdat:
    reader = csv.reader(bankdat, delimiter = ",")
    headers = next(reader, None)
    print(headers)
    # months = len(list(reader))
    # print(months)
    net = 0
    for row in reader:
        net = net + float(row[1])
        changes = [change for change in row[1]]
        print(changes)
        print(net)
        #change = 
## Total months

## Total net changes

## Average change

## Greatest Increase in Profits

## Greatest Decrease in Profits