def main():
    n = rg(1,9) #Beggining and end(actual) of the range we want to add together
    t = rs(n, 0,len(n)-1)
    print("The sum of the array is", t)
def rg(s,f): #generates the range into an array
    a = list(range(s,f+1))
    return a
def rs(l, b, e): #Uses recursion to add the numbers in the array together
    if b > e:
        return 0
    else:
        return l[b] + rs(l,b + 1, e) #adds the array and calls the function again
main()
