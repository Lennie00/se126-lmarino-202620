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




#working with a list--------------------------------------------------------
total_records = 0

machine_type = []

brand = []

proc = []

ram = []

first_hd = []

num_hd = []

second_hd = []

os = []

yr = []


#header------------------------------------------------------------------------
print(f"{'type':10}{'brand':10}{'proc':5}{'ram':5}{'1st_hd|':7}{'2nd_hd':10}{'os':5}{'yr':5}")
print("-" * 70)
with open("filehandling.csv") as csvfile: 

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        if rec[0] == "D":
            machine_type.append("Desktop")

        elif rec[0] == "L":
            machine_type.append("Laptop")

        else:
            machine_type.append("*ERROR*")


        if rec[1] == "DL":
            brand.append("Dell")

        elif rec[1] == "GW":
            brand.append("Gateway")

        elif rec[1] == "HP":
            brand.append("HP")

        else:
            brand.append("*ERROR*")

        #cpu
        proc.append(rec[2])
        #ram
        ram.append(rec[3])
        #first drive
        first_hd.append(rec[4])

        #rec 5

        if rec[5] == "1":
            num_hd.append(rec[5])
            second_hd.append("---")#no second hd
            os.append(rec[6])
            yr.append(rec[7])

        else:
            num_hd.append(rec[5])
            second_hd.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])




    #process through the lists------------------------------------for index in range/for index in listname


    for index in range (0,len(machine_type)):
        print(f"{machine_type[index]:10}{brand[index]:10}{proc[index]:5}{ram[index]:5}{first_hd[index]:7}{second_hd[index]:10}{os[index]:5}{yr[index]:5}")


    print("-" * 50)

    old_desktop = 0
    old_laptop = 0

    for i in range (0,len(machine_type)): # i mean index
        #count desktops and laptops that are to old (year <= 16)
        if int(yr[i]) <= 16:
            #machine to old
            if machine_type[i] == "Desktop":
                old_desktop += 1

            elif machine_type[i] == "Laptop":
                old_laptop += 1

            else:
                print(f"******You have an error in index {i} / data file line: {i + 1}******")


    print("\nMachines processed for replacment budget:")
    print(f"Desktop to replace: {old_desktop} @ 2k/each --->${old_desktop * 2000:.2f}")
    
    print(f"Laptop to replace: {old_laptop} @ 1.5k/each --->$ {old_laptop * 1500:.2f}")



       

    total_cost = (old_desktop * 2000) + (old_laptop * 1500)
    #print how many records-----------------------------------------------------------
    print(f"Total replacment Cost: ${total_cost:.2f}")


    #Done----------------------------------------------------------------------------------------------------------
    


   


   
    