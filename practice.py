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

a = 10
b = 10
op = '*'
result = calculator(a ,b ,op)
print(result)

