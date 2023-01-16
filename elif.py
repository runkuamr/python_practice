print("welcome to AAA school result protel")
name=input("enter the student name :")
reg_num=input("enter your register number")
tamil=int(input("enter your tamil mark:"))
english=int(input("enter your english mark:"))
maths=int(input("enter your maths mark:"))
physics=int(input("enter your physiscs mark:"))
chemistry=int(input("enter your chemistry mark:"))
total=tamil+english+maths+physics+chemistry
print("the total is :",total)
avg=total/5.0
print("the avg is :",avg)
if tamil>=35 and english>=35 and maths>=35 and physics>=35 and chemistry>=35:
    print( "result : pass")
    if avg>=91 and avg<100:
        print("coungralations your pass , your grade is A")
    elif avg>=81 and avg<=90:
        print("coungralations your pass , your grade is B")
    elif avg>=71 and avg<=80:
        print("coungralations your pass , your grade is c")
    elif avg>=61 and avg<=70:
        print("coungralations your pass , your grade is d")
    else:
        print("your pass")
else:
    print("sorry!, you are with heald , best of luck for nest time")
    print("\nthank you")


