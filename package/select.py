import package.function
import package.greet

def selectt():
    print("Enter 1 for subtraction and 2 for greeting")
    c=int(input("Enter the value : "))
    if c==1:
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        print(package.function.sub(a,b))
    elif c==2:
        print("Hello! ")
        s=str(input("Enter your name\n"))
        print(package.greet.greeting(s))
    else:
        print("Wrong choice")
