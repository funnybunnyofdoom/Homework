import random #Import the random library for Python

def main(): #declare the main definition
    index = 0 #Set index to 0
    lotteryList = list(range(1,8)) #initialize our list at 7 long

    while index < 7: #for 7 times do
        lotteryList[index] = random.randint(0,9) #insert random number into list in the index place
        index+=1 #increment index

    index = 0 #reset index

    while index < 7: #for seven times
        print(lotteryList[index]) #Print out the lottery place of the list
        index+=1 #increment index
    
main() #Call the main definition
    
