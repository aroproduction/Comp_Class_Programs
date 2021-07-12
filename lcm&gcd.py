# Program to find L.C.M of 2 numbers


def lcm(x, y):
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("What you want to calculate L.C.M OR G.C.D? (l/g): ")

if operator == 'l':
    print("The L.C.M of", num1, "&", num2, "is", lcm(num1, num2))
elif operator == 'g':
    print("The G.C.D of", num1, "&", num2, "is", gcd(num1, num2))




