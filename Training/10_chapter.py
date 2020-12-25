# Object oriented programming 
class Number:
    def sum(self):
        return self.a+self.b


num = Number()
num.a=10
num.b=20
s=num.sum()
print(s)


class Employee:
    company="Google" # class attribute


    # constructor
    def __init__(self,name , salary,age): # self can be written in nay value like sel or se .
        self.name=name
        self.salary=salary
        self.age=age
        print("Employee constructor is called on object instantiation!!")


    def printdata(self,signature):
        print(f"{self.name} --- {self.age} -- {self.salary} and {signature}")
    
    @staticmethod
    def staticm() :
        print("Statitc method")

emp=Employee("ravi","1 crore", 30)
print(emp.company)
Employee.company="facebook"
print(emp.company)
emp.salary=10 # object attributes
emp.age=20
emp.printdata("Signature") # equivalent to Employee.printdata(emp)

# static 
Employee.staticm()



