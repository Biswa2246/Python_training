#decision making

a = int(input())

if(a%3==0 and a%5==0):
    print(a," is a multiple of 3 and 5")
elif(a%3==0):
    print(a," is a multiple of 3")
elif(a%5==0):
    print(a," is a multiple of 5")
else:
    print("Invalid")

#------------------------------------------------------------------------

#loops
for i in range(101):
    print(i,end=' ')
print()

print("odd numbers")
for i in range(101):
    if(i%2!=0):
        print(i,end=' ')
print()
print("even numbers")
for i in range(101):
    if(i%2==0):
        print(i,end=' ')

print()
print("Reverse")
for i in range(100,0,-1):
    print(i,end=' ')
print()

print("odd numbers")
for i in range(100,0,-1):
    if(i%2!=0):
        print(i,end=' ')
print()
print("even numbers")
for i in range(100,0,-1):
    if(i%2==0):
        print(i,end=' ')

#------------------------------------------------------------------------

#break
for i in range(1,101):
    if(i==50):
        break
    print(i,end=' ')
else:
    print("else statement")

#------------------------------------------------------------------------

#continue
for i in range(1,101):
    if(i==50):
        continue
    print(i,end=' ')

#------------------------------------------------------------------------

#pass
for i in range(1,101):
    if(i==50):
        pass
    print(i,end=' ')

#------------------------------------------------------------------------

#functions

def function1():
    print("its a function")
function1()

def function2(a,b):
    print("a: ",a," b: ",b)
function2(10,20)

def function3(a,b):
    c=a+b
    return c
print("value returned",function3(10,20))

def function4(a,b):
    c=a+b
    return c
print("value returned",function4(10,20.2))

def function5(a,b):
    c=float(a)+b
    return c
print("value returned",function5('10',20))

#------------------------------------------------------------------------

#categories of functions based on arguments

#1: positional arguments

def function1(a,b,c,d):
    print("a: ",a," b: ",b," c: ",c," d: ",d)

function1(10,20,30,40)
#function1(10,20,30,40,50)
#function1(10,20,30)
function1(10,"20",30,40)
#------------------------------------------------------------------------
#2: keyword arguments

def function2(a,b,c,d):
    print("a: ",a," b: ",b," c: ",c," d: ",d)

function2(a=10,b=20,c=30,d=40)
function2(b=20,a=10,d=40,c=30)

#------------------------------------------------------------------------
#3: default arguments

def function3(name,rollno,branch,collegename="GIETU"):
    print(name,rollno,branch,collegename)
function3("jagannath",265,"CSE")
#------------------------------------------------------------------------
#4: variable numbers of arguments
    #function overloading

def function4(*var):
    for i in var:
        print(i,end=' ')

function4(10,20)
print()
function4(10,20,30)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50)


def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return sum

print(add(10,20))
print()
print(add(10,20,30))
print()
print(add(10,20,30,40))
print()
print(add(10,20,30,40,50))
num1=int(input(""))
num2=int(input(""))
num3=int(input(""))

#-----------------------------------------------------------

if num1==7:
    num4=num2*num3
    print(num4)
elif num2 == 7:
    num4=num3
    print(num4)
elif num3 == 7:
    print("-1")
else:
    exit()
#OUTPUT
5
6
7
-1

#---------------------------------------------------


#CURRENCY CALCULATOR
cur=input("enter currency")
amount=int(input("enter amount"))
value=0
if cur == "euro":
    value= (1/0.01417)*amount
    print(value)
elif cur == "british pound":
     value= (1/0.0100)*amount
     print(value)
elif cur == "austrilian dollar":
     value= (1/0.02140)*amount
     print(value)
elif cur == "canadian dollar":
     value= (1/0.02027)*amount
     print(value)
else:
    exit()
#OUTPUT
enter currencyeuro
enter amount10000
705716.3020465772


#-------------------------------------------------

#FLIGHT TICKET PROGRAM
adults=int(input("No. of Adults:"))
child=int(input("No. Of Child:"))
total_ticket=(adults*37550 + child*37550/3) + (adults*37550 + child*37550/3)*0.07
ticketwithdiscount=total_ticket-total_ticket*0.10
print("Total Ticket Cost:",ticketwithdiscount)

#OUTPUT
No. of Adults:5
No. Of Child:2
Total Ticket Cost: 204910.35






























     
