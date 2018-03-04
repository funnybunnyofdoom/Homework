#Anthony Antognazzi
#Python 2018SP CSC-221-01IN
#Car Test

import AntognazziA_CarClass #Load the class file

def main(): #Construct the main function
    Auto = AntognazziA_CarClass.Car(1990,"Honda") #Create the object
    for i in range(1,6): #Iterate 5 times.
        Auto.accelerate() #Call Accelerate
        print(Auto.get_speed()) #display get_speed
    for i in range(1,6): #Iterate 5 times
        Auto.brake() #call brake
        print(Auto.get_speed()) #display get_speed

main() #Call the main function
