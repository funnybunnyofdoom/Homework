def main():
    num1 = int(input('Enter an integer'))
    num2 = int(input('Enter another integer'))

    print("The greatest common divisor of")
    print("The two numbers is", gcd(num1,num2))

def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

main()
