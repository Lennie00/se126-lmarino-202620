#w2 text file handeling intro demo

#steo one:import the csv liabary (comma seperated values)
import csv

total_records = 0 #hold total number of records on file

#STEP 2:CONNECT TO FILE 
#-----connected to file-----------------------------------------------------
#include relative file path in open() - make sure to switch \ tpo /
with open("simple.csv") as csvfile:
    #make sure to indent inside of code block!
    # the colon : is a new code bloc

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile) 
    #file = entire data from file! organized ad records 


    #step 3:process through every record(row) in the file
    for record in file:
        #add +1 total_records to keep accurate count
        total_records += 1  #total_records = total_records + 1

       # print(record)   #entire row/record data asa list 

        name = record[0] #name field

        number = record[1] #number field

        color = record[2] #color field

        print(f"{name}'s number is {number} and they love the color {color}!")
    





#--disconnected from file-----------------------------------------------------------
print("---------------------------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")