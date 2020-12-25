# Conditional Expression 
a=45
a=4
if(a>3): 
        print("Value is greater than 3")
elif(a>7): 
        print("Vlaue s greater than 7")
else:
        print("Smaller")
                
if(a>3): 
        print("Value is greater than 3")
if(a>7): 
        print("Vlaue s greater than 7")
else:
        print("Smaller")
                

age=int(input("Enter your age"))
if(age>21 and age<34):
    print("1")
elif(age>18 or age<21):
    print("2")
elif(not age>21):
    print("3")
else:
    print("none")

d=None
if(d is None):
    print("yES")
else:
    print("No")

arr=[2,3,4]
print(3 in arr)    

text=input("Enter your text")
if("lottery ticket" in text):
 spam=True
elif("make money" in text):
 spam=True
elif("loan free" in text):
 spam=True
else:
    spam=False

print("Is it spam ?",spam)   


post="Hi htis is rAvI . you are taling about me"
print(post.casefold())

if('ravi' in post.casefold()):
    print("they are talking about ravi!!")
else:
    print("No , they are noe")

print(post.lower())
print(post.upper())