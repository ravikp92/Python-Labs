

# Functions 
def averagefn(marks):
    return (sum(marks)/4)

marks =[75,2,3,4]
average= averagefn(marks)

marks2 =[2,3,4,5]
average2= averagefn(marks2)
print(average,average2)

# default value of function 

def greet(name="Stranger"):
    print("Good Day ! ",name)

greet("Harry")
greet()

# Recursion 

def fact_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

print(fact_iter(5))

def fact_recur(n):
    if n==0 or n==1:
      return 1
    return n*fact_recur(n-1)

print(fact_recur(5))


def sumOfN(n):
    if n==0:
        return 0
    return n+sumOfN(n-1)

print(sumOfN(5))    

def removeandstrip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()

this= "  Ravi is best and awesome    "
n=removeandstrip(this,"and")
print(n.split())

