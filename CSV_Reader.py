
import csv
from statistics import mean


with open('table.csv','r') as csvfile:
    reader = csv.reader( csvfile )
    for row in reader:
        print(row)
