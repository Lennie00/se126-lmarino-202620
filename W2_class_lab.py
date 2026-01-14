#Lennie Marino
#Class Lab_2 W2 
#1/13/2026


#edit*********************************This was the only prompt I found, not sure if i had to make one up! :)


#prompt:The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
#can accommodate, and the number of people currently registered for the event. Write a program that
#displays all rooms that are over the maximum limit of people and the number of people that have to
#be notified that they will have to be put on the wait list. After the file is completely processed the
#program should display the number of records processed and the number of rooms that are over the
#limit.












#step one:import the csv liabary (comma seperated values)

import csv 
#define var
total_rec = 0 

#STEP 2:CONNECT TO FILE 
#-----connected to file-----------------------------------------------------
#include relative file path in open() - make sure to switch \ tpo /
#set up border for better looking table
print(f"{'FIRST':10}  {'LAST':10}  {'NUM':3}  {'CLASS1':7}  {'CLASS2'}")
print("-----------------------------------------------------------")
with open("unevenRecords.csv") as csvfile:
    #make sure to indent inside of code block!

    # the colon : is a new code block

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile)
    #file = entire data from file! organized ad records 

    #step 3:process through every record(row) in the file
    for rec in file:
        total_rec += 1

        first = rec[0]
        last = rec[1]
        num = int(rec[2]) #***** KEY
        class1 = rec[3]

        #IF num is 1, there is only 1 class listed (rec[3])
        #IF NUM is 2, there are two classes listed (rec[3], rec[4])

        if num == 2:
            class2 = rec[4]
        else:
            class2 = "-----"

        print(f"{first:10}  {last:10}  {num:1}    {class1:7}  {class2}")
        
#--disconnected from file-----------------------------------------------------------
print("-----------------------------------------------------------")
#closing message!Goodbyeeeeee----------
print(f"\nThere are {total_rec} students in the file.\n\n")
