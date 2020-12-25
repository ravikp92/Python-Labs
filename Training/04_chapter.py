# Create a list
a=[1,2,34,4,5,7]
# Modified list 
a[3]=2323
print(a)


# List of different of types 
b=[1,"asdas", 43.3, True]
print(b)


friends=["test","your","knowledges"]
print(friends[0:2])
print(friends[-2:])

l1=[1,2,3,1,2,34,2,123,0,12,2]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(8) # add at end of list
print(l1)

l1.insert(0,45)
print(l1)

l1.insert(2,1111) # insert at index
print(l1)

l1.pop(1) # remove at index
print(l1)

l1.remove(45) # remove element
print(l1)



# Tuples - can't be updated. Immutable
t=(1,2,1,1,1,3,3,4)
print(t)


t1=(1,)
print(t1)

print(t.count(1))
print(t.index(2))


m1=int(input("Enter number : "))
print(m1)

print(sum(t))