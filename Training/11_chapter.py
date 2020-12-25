# Inheritance 

# Single Inheritance 
class Employee:
    company="Google"

    def showdetails(self):
        print(f"This is an employee of {self.company}")
    
class Programmer(Employee):
    language="Python"
    def getLanguage(self):
        print(f"The language is {self.language}") 

    def showdetails(self):
        print(f"This is an programmer of {self.language}")

e=Employee()
e.showdetails()
p=Programmer()
p.getLanguage()
p.showdetails()
print(p.company)


# Multiple Inheritance 

class Emp:
    company="Visa"
    ecode=101

class Freelancer:
    company="Fever"
    level=1

class Test(Emp,Freelancer):
    name="ravi"

p1=Test()
print(p1.name)
print(p1.level)
print(p1.ecode)
print(p1.company) # class Test(Emp,Freelancer): Employee written first . so its company is called

# Multilevel Inheritance and 
#  and use of super 



class Emp1:
    company="Visa"
    ecode=101

    def __init__(self):
        print("..Initializing Emp1..")
    def takeBreath(self):
        print("Emp1 is breathing")

class Freelancer1(Emp1):
    company="Fever"
    level=1
    def __init__(self):
        super().__init__()
        print("..Initializing Emp1..")

    def takeBreath(self):
        super().takeBreath()
        print("freelancer1 is breathing")

class Test1(Freelancer):
    name="ravi"
    def takeBreath(self):
        #  super().takeBreath()
        print("test1 is breathing")

a=Emp1()
a.takeBreath()
b=Freelancer1()
b.takeBreath()
c=Test1()
c.takeBreath()


# class method 


class Emp2:
    company="Visa"
    salary=10
   
    @classmethod
    def getSalary(cls,salary):
        cls.salary=salary
        # print("Emp1 is breathing")


t=Emp2()
print(t.salary)
t.getSalary(45)
print(t.salary)
print(Emp2.salary)




# property decorators 

class Emp3:
    company="Google"
    salary=100
    salarybonus=10
    
    @property  # getter
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary

q=Emp3()
print(q.totalSalary)
q.totalSalary = 5800
print(q.salary)
print(q.salarybonus)


# Operator Overloading 

class Number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        return self.num+num2.num
    
    def __mul__(self,num2):
        return self.num*num2.num

    def __str__(self):
        return f"Number is {self.num}"

    def __len__(self):
        return 1

n1=Number(5)
n2=Number(4)
print(n1)
print(n2)
print(len(n1))
print(len(n2))
sum=n1+n2
multiply= n1*n2
print("Sum is :",sum)
print("Multiple is :",multiply)


# Complex numbers 
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary +c.imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=Complex(3,4)
c2=Complex(4,5)

print(c1+c2)