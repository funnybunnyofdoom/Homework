#Course Information
#Anthony Antognazzi
#Python Chapter 9 Exercise 1
#2/17/2018

def main(): #Main function of the program
    myCourses = {'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411} #Course rooms
    instCourses = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'} #Course Instructors
    timeCourses = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'} #Course times

    cont = True
    while cont:
        course = getCourse(myCourses)#Call the get course function to ask which course the user wants information on
        displayCourse(course, myCourses, instCourses, timeCourses) #Feed the course, and the dictionaries to the displayCourse function
        print("Continue? (y/n)") #Ask if user wishes to continue
        C = input() #Grap the choice from the user
        if C == 'n' or C == 'N': #Screen for no
            cont = False #End the loop on no

def getCourse(y): #This function gets the input from the user
    print("Please enter one of the following courses:")
    print('CS101, CS102, CS103, NT110, CM251')
    x = input()
    while x not in y: #Check for valid input
        print("Invalid Input. Please select from the list.")
        x = input() #store the input in x
    return x #Return user input to the function that called it

def displayCourse(CR,a,b,c): #Take in CR as the course and a,b, and c are respective dictionaries
    print("Room number:",a[CR]) #Print the room from dictionary a corresponsing to CR
    print("Instructor:",b[CR]) #Print the instructor from dictionary a corresponsing to CR
    print("Meeting Time:",c[CR]) #Print the meeting time from dictionary a corresponsing to CR
    

main() #Call the main function for the program
