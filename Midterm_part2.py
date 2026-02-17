#lennie marino
#se116 midterm part 2 --->choice 3 
#2/9/2026


#prompt------------------------------------------------------------------------------------
#Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
#been fully populated with file data, create a new list to hold a student ID value for each student. The first
#student in the file should have an ID of 10001, each student’s ID should be unique, and the ID values
#should not exceed 10021. Once the new list is populated, process through the five lists to display all of
#the student data to the user as well as the total number of records in the file.
#Once all of the data has been displayed, write all of the list data to a new file called
#‘midterm_choice3.csv’, where each student’s information is found on one record in the file and their
#data is separated by a comma (additional empty line in resulting file is okay).
#Finally, create a sequential search program that allows a user to repeatedly search the student database
#information stored in the lists based on the following menu:
#Student Search
#1. Search by LAST NAME
#2. Search by DEPARTMENT
#3. EXIT
#For option 1: When a searched-for item is found, print all data* in the program on the specific student
#from the lists. If they are not found, alert the user.
#For option 2: When a searched for item is found, print all data* in the program on all students that
#match the criteria. If no one matches the searched-for criteria, alert the user.
#The user should not be able to quit the search program unless they choose option 3, to exit.
#*All Data to print per employee if found:
#first name, last name, department, gpa, student ID


#start--------------------------------------------------------------------------------------------------------


#--IMPORT---------------------------------------------------------
import csv




#--MAIN EXECUTING CODE---------------------------------------------

# parallel lists
firstName = []
lastName = []
department = []
gpa = []
studentID = []

# connecting to the file with the with open
with open("students.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        firstName.append(rec[0])
        lastName.append(rec[1])
        department.append(rec[2])
        gpa.append(float(rec[3]))

# disconnected from file ---------------------------------------------------------------------------

# create student IDs starting at 10001 and go up from there
start_id = 10001
for i in range(0, len(firstName)):
    studentID.append(start_id + i)








# display all student data(header)
print(f"{'FIRST':10}  {'LAST':10}  {'DEPT':15}  {'GPA':4}  {'ID'}")
print("-------------------------------------------------------------------")

for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {department[i]:15}  {gpa[i]:4.2f}  {studentID[i]}")

print("-------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")





# Wrie the student data to the new file---------------------------------
file = open("midterm_choice3.csv", "w")

for i in range(0, len(firstName)):
    file.write(f"{firstName[i]},{lastName[i]},{department[i]},{gpa[i]},{studentID[i]}\n")
#make sure to close file
file.close()










# SEQUENTIAL SEARCH ------------------------------------------------
print("\tStudent Search Program")

answer = "y"

while answer == "y":
    print("\t~Search~")

    print("1. Search by last name")

    print("2. Search by department")
    
    print("3. Exit/Close down")

    search_type = input("Enter given values for search type [1-3]: ")

    # OPTION 1 -------------------------------------------------------------------------
    if search_type == "1":
        print("\tLAST NAME ")

        found = -1
        search_last = input("Enter the last name you want to find: ")

        for i in range(0, len(lastName)):
            if search_last.lower() == lastName[i].lower():
                found = i

        if found != -1:
            print("Student data:")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {department[found]:15}  {gpa[found]:4.2f}  {studentID[found]}")
        else:
            print("Student not found!")
            print("Please provide correct spelling!.")

    # OPTION 2 -----------------------------------------------------
    elif search_type == "2":
        print("\tDepartment search~")

        found = []
        search_dept = input("Enter the department you want to find: ")

        for i in range(0, len(department)):
            if search_dept.lower() == department[i].lower():
                found.append(i)

        if not found:
            print("No students found in that department.")
        else:
            print("students:")
            for i in range(0, len(found)):
                print(f"{firstName[found[i]]:10}  {lastName[found[i]]:10}  {department[found[i]]:15}  {gpa[found[i]]:4.2f}  {studentID[found[i]]}")

    # OPTION 3 -------------------------------------------------------------
    elif search_type == "3":
        print("\tEXIT")
        answer = "x"

    else:
        print("\t!INVALID ENTRY!")
#ask user if they want ti enter more entries !!!!!
    if search_type == "1" or search_type == "2":
        answer = input("Would you like to try a new search? [y/n]: ").lower()







#print goodbye message!!!!!!
print("\nThank you for using the search program, Come back again!\n")


