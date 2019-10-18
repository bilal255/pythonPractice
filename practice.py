#This program is a basic arithmatic calculator
#Defining caluculator function 
def calculator (num1 , num2 , oper):
    if(oper == '+'):
        return num1+num2
    elif(oper == '-'):
        return num1-num2
    elif (oper == '*'):
        return num1*num2
    elif (oper =='/'):
        return num1/num2
    else:
        return num1%num2

    
#declaring two vars and one operator character variable
v1 = int(input("Enter 1st number"))
v2 = int (input("Enter 2nd Number"))
#op stores and shows the output of the result
op = char(input("Enter the operator")

#calling calculator function to calculate the result of expression and printing result
result = calculator(a ,b ,op)
 
#Printing result
print(result)
#pragma once
