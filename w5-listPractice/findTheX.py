#Build a program to store the following file data into a list (one field of data = 1 list needed), then process the list and find the record that holds the "X" (capital X string value).  When finished, print the index of where the X was located. 

import csv 


charList = []

with open("C:/Users/KTRUCHON/Desktop/SE126_test/w5-listPractice/listPractice1.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        print(rec[0])