a=int(input("Enter First no:"))
b=int(input("Enter Second no:"))
choice=input("Enter your choice")
if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="*":
    print(a*b)
elif choice=="/":
    print(a/b)
    print(a//b)
else :
    print("invalid") 