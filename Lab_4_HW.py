#lennie marino
#se116 lab4_HW
#2-3-2026

#prompt-------------------------------------------------------------------------------------------------------------------

#Write a program that reads the data file (below) 
# and stores the data into 1D parallel lists 
# (remember, one list for every field).  Once the lists are populated 
# (and the file is "closed"), process the lists to reprint the file data, 
# record by record as they originally appear in the file.

#Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class 
# average. 

#While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter 
# grade into a list called 'let_avg'. Then, print each student's full information, record by record, including 
# average score and average letter equivalent.  After this print of the original file data from the lists, write
#  each student's data into a new file called compiled_class_info.csv. Once complete, print to the console the 
# total number of student's in the class along with the class numeric average to the console for the user.  
#After your final display using the 1D parallel lists, create a sequential 
# search program which allows the user to repeatedly utilize the following menu 
# of search types. When a searched for item is found, display all student data to 
# the console. When a search is compete and no matching data is found, alert the 
# user. Search options 1 and 2 should only show one found student, where search 
# option 3 should show a potential of multiple students.

#-----------------------------------------------------------------------------------------------------------------------

#Start--------------




#--IMPORTS---------------------------------------------------------
import csv
#--FUNCTIONS-------------------------------------------------------
def letter(num):
    '''This function is passed a numerica grade (num) and determines its letter grade equivalent, which is returned back to where the function was initially called.'''
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let ="F"
    else:
        let = "ERROR"

    return let #the 'let' value will literally replace the letter() call in main code
#--MAIN EXECUTING CODE---------------------------------------------

#create some empty lists 
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#connecting to the file 
with open("class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)
        firstName.append(rec[0])
        #parallel lists --> data dispersed across lists, connected by the same index
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file -------------------------------------------

#process the lists to create and store each student's numeric average as well as letter grade average, then display all data back to the user
num_avg = []        #holds student's numeric avg: (test1 + test2 + test3) / 3
let_avg = []        #holds student's letter avg: letter(num_avg) return

for i in range(0,len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))


#print field headers for display below
print(f"{'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("-----------------------------------------------------------------------------")
#processing through lists for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.1f}  {let_avg[i]}")
print("-----------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")

#WRITE STUDENT DATA TO A NEW FILE
file = open("class_grades-2.csv", "w") #creates file to write o

for i in range(0, len(firstName)):
    file.write(f"{firstName[i]},{lastName[i]},{test1[i]},{test2[i]},{test3[i]},{num_avg[i]},{let_avg[i]}\n")
    
file.close()


#SEQUENTIAL SEARCH-----------------------------------------------------------------
#build a repeatable program that allows a user to search through student records by first choosing a search type from a menu, performing the search based on the type, and displaying results
print("\tWelcome to the Student Search Program")

answer = input("Would you like to start your search? [y/n]: ").lower()

while answer == "y":
    #show user search menu 
    print("\t~Search Menu~")
    print("1. Search by LAST name")         #one search value found
    print("2. Search by LETTER grade")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
    if search_type == "1": #LAST NAME
        #sequential search - search for a student by their LAST name
        #this version of sequential search is looking for ONE item, a specific and unique LAST name
        
        print("\tLAST NAME SEARCH~")
        #step 1: set-up and gain search query
        found = -1  #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
        search_last = input("Enter the last name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(lastName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == lastName[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i #replace the invalid found value with the current index
                          

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2": #LETTER GRADE
        print("\tLETTER GRADE SEARCH")

       

        #step 1: set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the LETTER GRADE you wish to find: ") #grade we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(let_avg)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.upper() == let_avg[i]: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)
                

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_let} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{found[i]}:  {firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_avg[found[i]]}")
    elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()

#print a good bye message!!!-----------------------------------------------------------------------------
print("\nThanks for using the search program. Goodbye!\n")