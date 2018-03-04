def main():
    populationList = buildList() #Build the list from file
    print("The average change in population is: ",displayAVG(sum(populationList),len(populationList))) #Call the display average function with the populationlist sum
    print("The year with the greatest increase in population during the time period is: ",max(populationList)) #Get the max of the list
    print("The year with the smallest increase in population during the time period is: ",min(populationList)) #Get the min of the list

def buildList(): #Pulls the information from the file into the list
    file = open('USPopulation.txt','r') #Open target file
    popList = file.readlines() #Read the lines into the popList list
    file.close() #shut the file
    return popList #Return the list

def sum(inputList): #Add the items in the list together
    total = 0 #Set total to 0
    for value in inputList: #For each value in list,
        total += int(value)     #add em up, make sure to get int, there's a newline in there
    return total #Return the total number

def displayAVG(sumOfList,numOfList): #Get the 
    return sumOfList / numOfList #Return the average


main() #Call the main program
