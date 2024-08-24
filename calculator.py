def calculator(num1,num2,operator):
        if(operator=='+'):
            result=num1+num2
            print(f"{num1}+{num2}={result}")
        elif(operator=="-"):
            result=num1-num2
            print(f"{num1}-{num2}={result}")
        elif(operator=="*"):
            result=num1*num2
            print(f"{num1}*{num2}={result}")
        elif(operator=="/"):
            result=num1/num2
            print(f"{num1}/{num2}={result}")
        elif(operator=="^"):
            result=num1**num2
            print(f"{num1}^{num2}={result}")
        elif(operator=="%"):
            result=num1%num2
            print(f"{num1}%{num2}={result}")
        repeat=int(input("do you want to continue with the result(1-yes/0-no):"))
        if(repeat==1):
            num3=int(input("enter the number:"))
            operator=input("enter the operator")
            calculator(result,num3,operator)
print("welcome")
strat=1
while strat==1:
    num1=int(input("enter the number:"))
    num2=int(input("enter the number:"))
    operator=input("enter the operator:")
    calculator(num1,num2,operator)
    strat=int(input("do you want calculator again(1-yes/0-no):"))