#lennie marino
#se116 lab1
#1-6-2026

#prompt-----------------------------------------------------------------------------------

#You will be writing one Python file for this project - it is a program that determines whether a
#meeting room is in violation of fire regulations regarding the maximum room capacity. The
#program will accept the maximum room capacity and the number of people attending the
#meeting. If the number of people is less than or equal to the maximum room capacity, the
#program announces that it is legal to hold the meeting and tells how many additional people may
#legally attend. If the number of people exceeds the maximum room capacity, the program
#announces that the meeting cannot be held as planned due to the fire regulation and tells how
#many people must be excluded in order to meet the fire regulations. The user should be allowed
#to enter and check as many rooms as they would like without exiting the program.







#-----------Functions-----------------------------------
#function deffinition below- must define before calling function in main code 
def difference(people, max_cap):

    diff = max_cap - people 

    #the return value replaces the function call
    return diff #when diff < 0, to many people in room



def decision(a):
    #error trap loops!
    while a != "y" and a != "n":
        print("***INVALID ENTRY - 'y' or 'n' only!")
        a = input("\t\tWould you like to check another room? [y/n]: ").lower()
    
    return a
        
    










#--------main code----------------------------------------------

#function call below - actually the function
print(f"The difference is: {difference(22, 25)}")

print("\n\t\tWelcome to Lab #1\n")

answer= "y" 

while answer == "y":






    #● asks a user for the meeting name, room capacity, and people attending the meeting

    name = input("\nenter the name of the room: ")
    capacity = int(input(f"enter the max capacity for {name} room: "))
    attending = int(input(f"enter the number of people attending the meeting in {name} room: "))



    #● passes the room capacity and people attending to the difference() you wrote in Part 1

    diff_return = difference(attending, capacity)


    #● displays to the user whether the meeting meets fire safety or not (legal/illegal)
    #● also display how many people can be added or removed (remember: if different returns a negative
    #number, this is how many people should be removed) NOTE: all values related to people (adding/removing) should be displayed as positive values
    #- example: If the room capacity is 25 and 30 people are signed up for the meeting, the
    #program should tell the user that “5 people must be removed from the meeting to meet fire
    #regulations”; If the room capacity is 25 and 17 people are signed up for the meeting, the
    #program should tell the user that “8 people can be added to the meeting and still meet fire
    #regulations”
    if diff_return >= 0:
        #tell user legal and diff_return ppl can be added
        print(f"You meet the safty guidlines and can still add: {diff_return} people for your meeting!")
    else:

        print(f"You did not meet saftey guidline,you must remove {diff_return *-1} people or you can not hold your meeting!")
        #tell user illegal and diff_return *-1 ppl must be removed

    #● ask the user if they have another number to check; pass the value to the decision() you wrote in
    #Part 2 and continue the program based on that function’s return

    answer = input("\t\tWould you like to check another room? {y/n}: ").lower()

    answer = decision(answer)

    # ● Once the user is done checking meeting attendance, display a goodbye message
    if answer == 'n':
        print("Thank you for being safe and cheeking to see if you meet saftey requiremnts! Hope to see you back soon!")