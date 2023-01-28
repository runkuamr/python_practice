def add (a,b):
    return a + b
def sub (a,b):
    return a - b
def mul (a,b):
    return a * b
def div (a,b):
    return a / b
def mod (a,b):
    return a % b
print("Select Operator")
print("1.Addition")
print("2.Subtraction")
print("3.multiplicatin")
print("4.divisiobn")
print("5.modules")
while True:
    option = input("Enter option :(1,2,3,4,5)")
    if option in ("1,2,3,4,5"):
        try:
            a,b = map(int,input("Enter the value :").split(" "))
           
        except ValueError :
            print("Type error , Enter the Correct Value")
            continue
        if option == '1':
            print(a,"+",b,"=",int(add(a,b)))
        elif option == '2':
            print(a,"-",b,"=",sub(a,b))
        elif option == '3':
            print(a,"*",b,"=",mul(a,b))
        elif option == '4':
            print(a,"/",b,"=",div(a,b))
        elif option == '5':
            print(a,"%",b,"=",mod(a,b))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
    

