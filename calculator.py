def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "can't didvide by zero!!"
    return a/b
def calculator():
    print("simple CLI calculator")
    while True:
        print("\nChoose operation")
        print("1.add(+)")
        print("2.sub(-)")
        print("3.multi(*)")
        print("4.divide(/)")
        print("5.Exit")

        choice=input("Enter choice(1-5):")
        if choice=="5":
              print("exit")
        num1=float(input("Enter 1st number:"))
        num2=float(input("Enter 2nd number:"))
        if choice=="1":
            print(f"Result:{add(num1,num2)}")
        elif choice=="2":
            print(f"Result:{sub(num1,num2)}")
        elif choice=="3":
            print(f"Result:{multi(num1,num2)}")
        elif choice=="4":
            print(f"Result:{divide(num1,num2)}")
        else:
            print("invalid")
if __name__=="__main__":
    calculator()
              


    
