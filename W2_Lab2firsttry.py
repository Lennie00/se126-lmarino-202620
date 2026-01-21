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


with open("filehandling.csv") as csvfile: 

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile)


    count = 0


    #headers
    print(f"{'Type':<10}{'Brand':<10}{'Cpu':<10}{'Ram':<5}"
          f"{'1st Disk':<10}{'No HDD':<8}{'2nd Disk':<10}"
          f"{'OS':<5}{'YR':<5}")
    
    print("-" * 75)


    for rec in file :
        data = rec

        comp_type = data[0] 

        brand = data[1]

        cpu = data[2]

        ram = data[3]

        first_disk = data[4]

        num_hdd = int(data[5]) 


        #if one hd
        if num_hdd == 1:
            second_disk = ""
            os = data[6]
            year = data[7]

            #if two hdd
        else:
            second_disk = data[6]
            os = data[7]
            year = data[8]

        print(f"{comp_type:10}  {brand:10}  {cpu:10}    {ram:5}  {first_disk:10}  {num_hdd:8}")


        
        

        count += 1

    print("\nToatal number of computers:", count)
                        







   
    