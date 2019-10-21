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
#INCLUDE Irvine32.inc
.data
msg1 dword "you are eligible",0
msg2 dword "you are not eligible",0
b dword "bsc",0
a dword 22
age dword ?
qual dword ?
.code
mov eax,0
call readint
mov age,eax
call writestring
mov edx,offset qual
cmp age,a
jmp m2
cmp qual,b
je m1
m2:
mov edx,offset b
cmp qual,b
jmp skip
m1: 
mov edx,offset msg1
call writestring
skip:
mov edx,offset msg2
call writestring
exit 
main endp
end main
    
#declaring two vars and one operator character variable and operator
a = int(input("Enter 2st number"))
b = int (input("Enter 2nd Number"))
op = char(input("Enter the operator")

#calling calculator function to calculatr the result of expression and printing result
result = calculator(a ,b ,op)
 
#Prinintg result
print(result)

