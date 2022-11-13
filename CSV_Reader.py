
import csv
from statistics import mean


with open('table.csv','r') as csvfile:
    reader = csv.reader( csvfile )
    with open('mean_table.csv', 'w') as out_meanfile:
        for row in reader:
            #print(row)
            name = row[0]
            mean_grade = mean((float(grade) for grade in row[1:])) #generator experation 

        
