#lennie marino
#se116 lab3_HW
#1-28-2026

#prompt-----------------------------------------------------------------------------------
#This lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows:

#(Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3)

#Construct a program that will analyze potential voters. The program should generate the following totals:

#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.
#write the Voter Registration Lab utilizing the data from the file voters.csv.  
# Store the field data into respective 1D lists, and then process the lists to determine the 4 final
#  output values (make sure they are clearly labeled!). This final solution should have NO input() statements 
# and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you 
# would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to 
# connect to a file and store data into lists, then use a for loop to process each voter and their data to find 
# the 4 totals.

#Number of individuals not eligible to register.
#if age < 18: 
#Number of individuals who are old enough to vote but have not registered.
#if age >= 18 and registered == "N":
#Number of individuals who are eligible to vote but did not vote.
#if age >= 18 and registered == "Y" and voted == "N":
#Number of individuals who did vote.
#if age >= 18 and registered == "Y" and voted == "Y":
#Number of records processed.
#total_records OR len(listName)
 

#Your final solution file should work for the csv file included, or any other file with the same fields and data formatting. 

 

#start
#--------------------------------------------------------------------------------------------------------------------

#step one:import the csv liabary (comma seperated values)

import csv 
#-------------------------------------------------------------------------------------------------------
#acess file
#main execute code-------------------------------------------------------------------

#working with a list--------------------------------------------------------
id_list = []
age_list = []
registered_list = []
voted_list = []


#----------------------------------------------------------------------
#var
not_eligible = 0
not_registered = 0
did_not_vote = 0
did_vote = 0


#-------------------------------------------------------------

with open("voters_202040.csv") as csvfile: 

    #allows the csv reader to access amd read the file
    file = csv.reader(csvfile)

    for rec in file:
        id_list.append(rec[0])

        age_list.append(int(rec[1])) 
        # convert age to (int) cause it only makes sense
        registered_list.append(rec[2])

        voted_list.append(rec[3])

    #-----------------------------------------------
    #index  #process through the lists------------------------------------for index in range/for index in listname
    for i in range(len(id_list)):

        age = age_list[i]

        registered = registered_list[i]

        voted = voted_list[i]


    #------------------------------------------------------------
    #if/elif staments
        if age < 18:
            not_eligible += 1
        elif age >= 18 and registered == "N":
            not_registered += 1
        elif age >= 18 and registered == "Y" and voted == "N":
            did_not_vote += 1
        elif age >= 18 and registered == "Y" and voted == "Y":
            did_vote += 1
        #make sure statments stay in loop!




#print statment-------------------------------------------------------------------------

print("Voters Poll")
print("----------------------------------------------")
print(f"Number of individuals not eligible to register: {not_eligible}")

print(f"\nNumber of individuals old enough but not registered: {not_registered}")

print(f"\nNumber of individuals eligible but did not vote: {did_not_vote}")

print(f"\nNumber of individuals who did vote: {did_vote}")

print(f"\nNumber of records processed: {len(id_list)}")

print("----------------------------------------------")


#End
#-----------------------------------------------------------------------------------------------
