# Loops 

i=0

while i<10:
    print("Yes"+str(i))
    i=i+1

print("Done")

fruits=['Banana','Apple','grapes','watermelon']
j=0
while(j<len(fruits)):
    print(fruits[j])
    j=j+1

for item in fruits:
    print(item)

for k in range(1,9,2):
    print(k)

# for loop with else 

for k in range(1,9,2):
    print(k)
else:
    print("Completed. Exhausted loop")


# break statment 
for o in range(1,9):
    print(o)
    if o==5:
        break
else:
    print("Completed. Exhausted loop")  


# continue statment - odd number
for o1 in range(1,9):
   
    if o1%2==0:
        continue
    print(o1)
else:
    print("Completed. Exhausted loop")  

# pass statment - null . do nothing- 

for o1 in range(1,9):
     pass

# multiplication of number 

number=int(input("Enter the number: "))
for n1 in range(1,11):
    print(f"{number}X{n1}={number*n1}")

#  name start with s 
str=['start','hoal','sohan']

for st in str:
    if st.startswith("s"):
        print("Hello :", st)

primen=int(input("Enter the number: "))
prime= True
for p1 in range(2,primen):
    if(primen%p1==0 and primen!=2):
        prime=False
        break
if prime:
    print("Number is prime")
else :
    print("Number is not prime")


#  print factorial 

fact=int(input("Enter the number: "))
factorial=1
for f1 in range(1,fact+1):
    factorial=factorial*f1
print(f"Factorial of number is {factorial}")


# Print star pattern 

'''
*
**
***
'''

starcount=int(input("Enter start count: "))

for i2 in range(starcount):
    print("*"*(i2+1))
# Print star pattern 

'''
     *
    ***
   *****
'''
starcount2 = int(input("Enter start count: "))   

for i3 in range(starcount2):
    print(" " * (starcount2-i3-1),end="")
    print("*" * (2*i3+1),end="")
    print(" " * (starcount2-i3-1))
