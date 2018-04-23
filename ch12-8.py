def main():
    listOfNumbers = rangeGen(1,10)
    theSum = sumOfNums(listOfNumbers,0,len(listOfNumbers)+1)
    print("The sum is ", theSum)

def rangeGen(Start,fin):
    array = list(range(Start,fin+1))
    return array

def sumOfNums(ARR,start,end):
    if start > end:
        return 0
    else:
        return ARR[start] + sumOfNums(ARR, start + 1, end)

main()
    
