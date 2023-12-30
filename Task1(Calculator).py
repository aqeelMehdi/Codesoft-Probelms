num1=int(input("Enter first number: "))
num2=int(input("Enter Second number: "))

operator=str(input("Enter the operator: "))



def Calculator(num1,num2,operator):

    if operator=="+":
        result=num1+num2
        print("The sum of two numbers is:",result)

    elif operator=="-":
        result=num1-num2
        print("The subtraction of two numbers is:",result)

    elif operator=="*":
        result=num1*num2
        print("The product of two numbers is:",result)

    elif operator=="/":
        result=num1/num2
        print("The division of two numbers is:",result)
        
Calculator(num1,num2,operator)