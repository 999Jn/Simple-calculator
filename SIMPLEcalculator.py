#were gonna get 2 inputs and an operator

#if statement=


num1=int(input("Enter a value:"))
num2=int(input("Enter a value:"))
op=input("Enter an operator:")

if op=="+":
    print("The addition is" ,num1+num2)

#if user wants to subtract
elif op=="-":
    print("The subtraction is",num1-num2)

elif op=="*":
    print("The multiplication is",num1*num2)

elif op=="/":
    print("The absolute is" ,abs(num1/num2))
else:
    print("Invalid operator")


