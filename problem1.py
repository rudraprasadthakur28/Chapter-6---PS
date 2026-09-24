a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))

if(a>b and a>c and a>d) :
    print("The greatest number is a: ", a)

elif(b>a and b>c and b>d) :
    print("The greatest number is b: ", b)

elif(c>b and c>a and c>d) :
    print("The greatest number is c: ", c)

elif(d>b and d>c and d>a) :
    print("The greatest number is d: ", d)