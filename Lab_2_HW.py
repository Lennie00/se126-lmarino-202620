#Lennie Marino
#1/20/2026
#W2_Lab2




#Prompt-You have been asked to produce a report that lists all the computers in the csv file
#filehandling.csv.
#Your report should look like the following sample output.
#The last line should print the number of computers in the file.Each row will have 8 or 9 columns. The number of columns depends on how many hard disk drives a
#computer has.


#-------------------------------------------------------------------------------------------------------------------------


#step one:import the csv liabary (comma seperated values)

import csv 
#-------------------------------------------------------------------------------------------------------
#acess file
#main execute code-------------------------------------------------------------------

total_records = 0
#header------------------------------------------------------------------------
print(f"{'type':10}{'brand':10}{'proc':5}{'ram':5}{'first_hd|':7}{'second_hd':10}{'os':5}{'yr':5}")
print("-" * 70)
with open("filehandling.csv") as csvfile: 

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        if rec[0] == "D":
            machine_type = "Desktop"

        elif rec[0] == "L":
            machine_type = "Laptop"

        else:
            machine_type = "*ERROR*"


        if rec[1] == "DL":
            brand = "Dell"

        elif rec[1] == "GW":
            brand = "Gateway"

        elif rec[1] == "HP":
            brand = "HP"

        else:
            brand = "*ERROR*"

        #cpu
        proc = rec[2]
        #ram
        ram= rec[3]
        #first drive
        first_hd = rec[4]

        #rec 5

        if rec[5] == "1":
            num_hd =rec[5]
            second_hd = "---"#no second hd
            os = rec[6]
            yr = rec[7]

        else:
            num_hd = rec[5]
            second_hd = rec[6]
            os = rec[7]
            yr = rec[8]


        #display machine data

        print(f"{machine_type:10}{brand:10}{proc:5}{ram:5}{first_hd:7}{second_hd:10}{os:5}{yr:5}")
    #print how many records-----------------------------------------------------------
    print("\nToatal number of records:", total_records)
    


   


   
    