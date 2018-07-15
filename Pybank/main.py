import os
import csv


Pybank_csv = os.path.join( "Resources", "budget_data.csv")

totalmonths = 0
totalprofit = 0
max = 0
min = 0
lastmonth = 0

with open(Pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
      
       totalmonths = totalmonths + 1
       totalprofit = totalprofit + int(row[1])
       averagechage = round( int(totalprofit) / int(totalmonths),2)
       
     
       change = int(row[1])- lastmonth
       lastmonth = int(row[1])
    
       
       if change > max:
        max = change
        maxmonth = row[0]
       if change < min:
        min = change
        minmonth =row[0]
      
    print (totalmonths)
    print (totalprofit)
    print (averagechage)
    print(maxmonth)
    print(max)
    print(minmonth)
    print(min)
text_file = open("Output.txt", "w")                 
text_file.write(str(totalmonths)+"\n")
text_file.write(str(totalprofit)+"\n")
text_file.write(str(averagechage)+"\n")
text_file.write(str(maxmonth)+"($"+str(max)+")"+"\n")
text_file.write(str(minmonth)+"($"+str(max)+")"+"\n")

    

    