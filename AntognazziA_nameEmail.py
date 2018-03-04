#9-8 Name and E-mail Address
#Anthony Antognazzi
#2/17/2018

import os.path #This will allow the program to check to see if the file exists.
import pickle #Allows us to pickle and unpickle the dictionary

def main():
    PB = {} #Empty phonebook
    PB = retrieve() #Fill phonebook from file
    menu(PB) #Give the user options, feed in the phonebook

def menu(phonebook): #Build a menu, get the user choice, and call that function
    print("Please make a selection:")
    print("1) Look up an E-mail address")
    print("2) Add an E-mail address")
    print("3) Change an existing E-mail address")
    print("4) Delete a name or a E-mail address")
    print("5) Exit")
    choice = input() #Ask the user for their decision. convert input into int
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            lookup(phonebook)
        elif choice == 2:
            add()
        elif choice == 3:
            change(phonebook)
        elif choice == 4:
            delete(phonebook)
        elif choice == 5:
            return
        else :
            print("Please select a valid option")
            main()
    else:
        main() 

def lookup(ph):
    print("Please enter the username to search")
    S = input()
    if S in ph: #Check to see if the input is in the dict
        print(ph[S]) #If so, then print the address
    else:
        print(S," Could not be found.")
    main() #Return to the main program
    

def add():
    name = ''
    address = ''
    print("Please enter a name")
    name = input() #Pull input into name
    print("Please enter an e-mail address")
    address =  input() #Pull input into address

    pBook = retrieve() #Call the retrieve function to load the file and get the list
    if pBook == False: #If there is no file, make a dict
        pBook = {}
    pBook[name] = address #Add the name and address to the dict
    save(pBook) #Call the save function to put the phonebook in the file

    main() #return to main program

def change(ph):
    print("What record would you like to change?")
    key = input() #Pull input to change into key
    if key not in ph: #If the record to change isn't found
        print("That record was not in the phonebook.")
    else:
        value = ph.pop(key) #Pop off the item to change
        print(value," ",key) #Display the item to change
    print("Please enter the new name")
    key = input() #Get the new name
    print("Please enter an e-mail address")
    value = input() #Get the new sddress
    print("Saving your entry.")
    ph[key] = value #Add the name and address
    save(ph) #Save the dictionary
    main() #return to main

def delete(Pb):
    print("Please enter the name you wish to delete")
    delete = input() #Get the key to delete
    value = Pb.pop(delete) #Pop off the item to delete
    print("Would you like to delete ",delete," ",value,"? (Y/N)") #Display the item to delete
    choice = input() #Get the option
    if choice == 'y' or choice == 'Y': #Determine whether or not to delete
        save(Pb) #Save the dictionary
    main() # Return to main

def save(p):
    file = open('phonebook.dat', 'wb') #Open the phonebook file for writing
    pickle.dump(p,file) #Dump the p dictionary into file
    file.close() #Close the file

def retrieve():
    if os.path.exists('phonebook.dat'): #Check to see if the file exists
        file = open('phonebook.dat','rb') #Open the file to read
        pb = pickle.load(file) #Unpickle the file
        file.close() #Close the file
        return pb #Return the unpickled dictionary from the file
    else:
        print("Phonebook doesn't exist. Add record first")
        pb = {'':''}
        return False


main() #Call the main program
