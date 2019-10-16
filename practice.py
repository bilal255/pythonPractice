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

    
#declaring two vars and one operator character variable and operator
a = int(input("Enter 2st number"))
b = int (input("Enter 2nd Number"))
op = char(input("Enter the operator")

#calling calculator function to calculatr the result of expression and printing result
result = calculator(a ,b ,op)
 
#Prinintg result
print(result)

