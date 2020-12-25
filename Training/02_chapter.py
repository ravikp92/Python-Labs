a1="ravi"
# valid
a2='ravi'
#valid
a3='''ravi'''

a_122='valid varibale name'
_122='valid varibale name'
b=23
c=45.3

d= True
e=None
# printing variables
print(a1)
print(a2)
print(a3)
print(b)
print(c)
print(d)
print(e)

# printing data type of variables - using type
print(type(a1))
print(type(a2))
print(type(a3))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Operators 
# Arithmetic Operators
print('The value of 3+4 is ',3+4)

#Assignment operators
a11=7
a11/=2
print('The value of a11 is ',a11)

# Comparison operator
print(b>a11)

# Logical operators

bool1= True
bool2=False
print(" Value of and is ",(bool1 and bool2))

print(" Value of or is ",(bool1 or bool2))

print(" Value of not is ",(not bool2))


# type casting

tp= "2345"
tp =int(tp)
print(type(tp))
print(tp+9)

print(str(31))
print(int("345"))
print(float(32))


# Input ()

name=input("Enter your name :")
print(type(name)) # always input is a string
print(name)



num1=input("Enter 1st number: ")
num2=input("Enter 2nd number: ")
num1=int(num1)
num2=int(num2)
print("Average of 1st and 2nd is :", (num1+num2)/2)